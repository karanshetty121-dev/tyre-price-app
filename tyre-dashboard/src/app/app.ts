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
}
