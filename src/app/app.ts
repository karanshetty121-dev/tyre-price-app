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
  searchQuery = signal<string>('');
  
  // Spec Filters
  widths = signal<string[]>([]);
  aspects = signal<string[]>([]);
  constructions = signal<string[]>([]);
  diameters = signal<string[]>([]);
  loadSpeeds = signal<string[]>([]);

  selectedBrand = signal<string>('All');
  selectedWidth = signal<string>('All');
  selectedAspect = signal<string>('All');
  selectedConstruction = signal<string>('All');
  selectedDiameter = signal<string>('All');
  selectedLoadSpeed = signal<string>('All');
  
  loading = signal<boolean>(true);
  error = signal<string | null>(null);

  // Editing State
  editingId = signal<number | null>(null);
  editForm = signal<any>(null);

  filteredTyres = computed(() => {
    const allTyres = this.tyres();
    const query = this.searchQuery().toLowerCase().trim();
    const brand = this.selectedBrand();
    const width = this.selectedWidth();
    const aspect = this.selectedAspect();
    const construction = this.selectedConstruction();
    const diameter = this.selectedDiameter();
    const loadSpeed = this.selectedLoadSpeed();

    return allTyres
      .map((tyre, index) => ({ ...tyre, originalIndex: index }))
      .filter(t => {
        const matchesBrand = brand === 'All' || t.Brand === brand;
        const matchesWidth = width === 'All' || t._width === width;
        const matchesAspect = aspect === 'All' || t._aspect === aspect;
        const matchesConst = construction === 'All' || t._const === construction;
        const matchesDiam = diameter === 'All' || t._diam === diameter;
        const matchesLS = loadSpeed === 'All' || t._ls === loadSpeed;
        
        const q = query.toLowerCase();
        const fullSize = t['Tyre Size'] ? t['Tyre Size'].toString().toLowerCase() : '';
        const pattern = t['Pattern'] ? t['Pattern'].toString().toLowerCase() : '';
        const matchesQuery = !query || fullSize.includes(q) || pattern.includes(q);
        
        return matchesBrand && matchesWidth && matchesAspect && matchesConst && matchesDiam && matchesLS && matchesQuery;
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
      let data = null;

      // 1. Try to load from Cloud Database (Skip if on localhost without proxy, or handle errors)
      try {
        const cloudResponse = await fetch('/api/tyres');
        if (cloudResponse.ok) {
          const contentType = cloudResponse.headers.get('content-type');
          if (contentType && contentType.includes('application/json')) {
            const cloudData = await cloudResponse.json();
            if (cloudData && !cloudData.status) {
              data = cloudData;
            }
          }
        }
      } catch (apiError) {
        console.log('Cloud API not available locally, falling back to master file.');
      }
      
      // 2. Parse and Enrich Data
      const enrichedData = data.map((t: any) => {
        // Regex to handle various formats: "145 70 R12 69S", "155 R13", "195 65 R15 91H"
        const sizeStr = (t['Tyre Size'] || '').toString();
        const parts = sizeStr.split(/\s+/);
        
        let width = 'N/A', aspect = 'N/A', construction = 'N/A', diameter = 'N/A', ls = 'N/A';
        
        // Simple heuristic parser
        parts.forEach(p => {
          if (/^\d{3}$/.test(p)) width = p;
          else if (/^\d{2}$/.test(p) && width !== 'N/A' && diameter === 'N/A') aspect = p;
          else if (/^[A-Z]{1,2}$/.test(p)) construction = p;
          else if (/^R\d{2}$/.test(p)) { construction = 'R'; diameter = p.substring(1); }
          else if (/^\d{2}$/.test(p) && diameter === 'N/A') diameter = p;
          else if (p.length >= 2 && /[0-9]{2}[A-Z]/.test(p)) ls = p;
        });

        // Fallback for R12, R13 etc if split didn't catch it
        if (construction === 'N/A' && sizeStr.includes(' R')) construction = 'R';

        return { ...t, _width: width, _aspect: aspect, _const: construction, _diam: diameter, _ls: ls };
      });

      this.tyres.set(enrichedData);
      
      const uniqueBrands = ['All', ...new Set(enrichedData.map((t: any) => t.Brand))].sort();
      this.brands.set(uniqueBrands as string[]);

      // Extract unique specs for filters
      const getUnique = (key: string) => ['All', ...new Set(enrichedData.map((t: any) => t[key]))].filter(v => v !== 'N/A').sort();
      
      this.widths.set(getUnique('_width'));
      this.aspects.set(getUnique('_aspect'));
      this.constructions.set(getUnique('_const'));
      this.diameters.set(getUnique('_diam'));
      this.loadSpeeds.set(getUnique('_ls'));
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
