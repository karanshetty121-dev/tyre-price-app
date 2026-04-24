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
  username = signal<string>('');
  password = signal<string>('');
  loginError = signal<string | null>(null);

  // Constants (In a real app, these would be in an environment file or backend)
  private readonly AUTH_USER = 'admin';
  private readonly AUTH_PASS = 'motofinez2026'; // Based on your shop's new year

  tyres = signal<any[]>([]);
  brands = signal<string[]>([]);
  selectedBrand = signal<string>('All');
  searchQuery = signal<string>('');
  
  loading = signal<boolean>(true);
  error = signal<string | null>(null);

  filteredTyres = computed(() => {
    let result = this.tyres();
    const query = this.searchQuery().toLowerCase().trim();
    const brand = this.selectedBrand();

    if (brand !== 'All') {
      result = result.filter(t => t.Brand === brand);
    }

    if (query) {
      result = result.filter(t => {
        const size = t['Tyre Size'] ? t['Tyre Size'].toString().toLowerCase() : '';
        const pattern = t['Pattern'] ? t['Pattern'].toString().toLowerCase() : '';
        return size.includes(query) || pattern.includes(query);
      });
    }

    return result;
  });

  async ngOnInit() {
    // Check for existing session
    const session = localStorage.getItem('mf_session');
    if (session === 'true') {
      this.isLoggedIn.set(true);
    }

    try {
      const response = await fetch('/tyres.json');
      if (!response.ok) throw new Error('Failed to load data');
      const data = await response.json();
      
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
    if (this.username() === this.AUTH_USER && this.password() === this.AUTH_PASS) {
      this.isLoggedIn.set(true);
      this.loginError.set(null);
      localStorage.setItem('mf_session', 'true');
    } else {
      this.loginError.set('Invalid credentials. Please try again.');
    }
  }

  logout() {
    this.isLoggedIn.set(false);
    localStorage.removeItem('mf_session');
    this.password.set(''); // Clear password
  }
}
