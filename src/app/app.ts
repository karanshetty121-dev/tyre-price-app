import { Component, OnInit, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App implements OnInit {
  title = 'Tyre Price Dashboard';
  
  // Auth State
  isLoggedIn = signal<boolean>(false);
  userRole = signal<'admin' | 'viewer' | null>(null);
  username = signal<string>('');
  password = signal<string>('');
  loginError = signal<string | null>(null);

  // User Accounts
  private readonly ACCOUNTS = [
    { username: 'karanshetty', password: 'Shetty@1992!', role: 'admin' as const },
    { username: 'motofinez', password: 'moto2026', role: 'viewer' as const }
  ];

  tyres = signal<any[]>([]);
  brands = signal<string[]>([]);
  selectedBrand = signal<string>('All');
  searchQuery = signal<string>('');
  
  loading = signal<boolean>(true);
  error = signal<string | null>(null);

  // Editing State
  editingId = signal<number | null>(null);
  editForm = signal<any>(null);

  filteredTyres = computed(() => {
    const allTyres = this.tyres();
    const query = this.searchQuery().toLowerCase().trim();
    const brand = this.selectedBrand();

    return allTyres
      .map((tyre, index) => ({ ...tyre, originalIndex: index }))
      .filter(t => {
        const matchesBrand = brand === 'All' || t.Brand === brand;
        const size = t['Tyre Size'] ? t['Tyre Size'].toString().toLowerCase() : '';
        const pattern = t['Pattern'] ? t['Pattern'].toString().toLowerCase() : '';
        const matchesQuery = !query || size.includes(query) || pattern.includes(query);
        return matchesBrand && matchesQuery;
      });
  });

  async ngOnInit() {
    // Check for existing session
    const session = localStorage.getItem('mf_session');
    const role = localStorage.getItem('mf_role') as 'admin' | 'viewer' | null;
    if (session === 'true' && role) {
      this.isLoggedIn.set(true);
      this.userRole.set(role);
    }

    try {
      // 1. Try to load from Cloud Database
      const cloudResponse = await fetch('/api/tyres');
      const cloudData = await cloudResponse.json();
      
      let data;
      if (cloudData && !cloudData.status) {
        // We have cloud data! Use it.
        data = cloudData;
      } else {
        // First time or empty database, load from local master file
        const localResponse = await fetch('/tyres.json');
        if (!localResponse.ok) throw new Error('Failed to load master data');
        data = await localResponse.json();
        
        // Optionally seed the database with master data if admin is logged in
        // (We'll let the first save handle this naturally)
      }

      this.tyres.set(data);
      
      const uniqueBrands = ['All', ...new Set(data.map((t: any) => t.Brand))];
      this.brands.set(uniqueBrands as string[]);
    } catch (e: any) {
      this.error.set(e.message);
    } finally {
      this.loading.set(false);
    }
  }

  selectBrand(brand: string) {
    this.selectedBrand.set(brand);
  }

  onLogin() {
    const user = this.ACCOUNTS.find(a => a.username === this.username() && a.password === this.password());
    
    if (user) {
      this.isLoggedIn.set(true);
      this.userRole.set(user.role);
      this.loginError.set(null);
      localStorage.setItem('mf_session', 'true');
      localStorage.setItem('mf_role', user.role);
    } else {
      this.loginError.set('Invalid credentials. Please try again.');
    }
  }

  logout() {
    this.isLoggedIn.set(false);
    this.userRole.set(null);
    localStorage.removeItem('mf_session');
    localStorage.removeItem('mf_role');
    this.password.set('');
  }

  startEdit(index: number, tyre: any) {
    if (this.userRole() !== 'admin') return;
    this.editingId.set(index);
    this.editForm.set({ ...tyre });
  }

  cancelEdit() {
    this.editingId.set(null);
    this.editForm.set(null);
  }

  async saveEdit(index: number) {
    const updatedTyres = [...this.tyres()];
    updatedTyres[index] = { ...this.editForm() };
    
    // Optimistic Update
    this.tyres.set(updatedTyres);
    this.editingId.set(null);
    this.editForm.set(null);

    try {
      // Persist to Cloud Database
      const response = await fetch('/api/tyres', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ data: updatedTyres })
      });
      
      if (!response.ok) throw new Error('Failed to save to cloud');
      console.log('Price synchronized to cloud successfully');
    } catch (e: any) {
      console.error('Cloud Sync Error:', e);
      this.error.set('Cloud Sync Error: ' + e.message + '. Please check your connection.');
    }
  }

  async resetData() {
    if (confirm('Are you sure you want to reset all cloud data? This will revert to the original price list for EVERYONE.')) {
      try {
        const response = await fetch('/tyres.json');
        const originalData = await response.json();
        
        const apiResponse = await fetch('/api/tyres', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ data: originalData })
        });

        if (apiResponse.ok) {
          window.location.reload();
        }
      } catch (e: any) {
        this.error.set('Failed to reset cloud data.');
      }
    }
  }

  exportData() {
    // Remove originalIndex before exporting
    const exportData = this.tyres().map(({ originalIndex, ...rest }) => rest);
    const dataStr = JSON.stringify(exportData, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);
    
    const exportFileDefaultName = 'tyres_updated.json';
    
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
  }
}
