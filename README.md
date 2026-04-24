# 🏁 MOTO FINEZ Master Data Dashboard

A high-performance, professional tyre price intelligence dashboard built for **MOTO FINEZ**. This application provides a sleek, modern interface for shop staff to quickly search and verify master pricing data across major tyre brands.

![UI Theme](https://img.shields.io/badge/UI-Dark_Intelligence-49DE95?style=for-the-badge)
![Tech](https://img.shields.io/badge/Angular-21-DD0031?style=for-the-badge&logo=angular)
![Styling](https://img.shields.io/badge/Tailwind_CSS-4-38B2AC?style=for-the-badge&logo=tailwind-css)

---

## 🚀 Key Features

- **🔍 Instant Intelligence**: High-speed, "search-as-you-type" functionality for tyre sizes, patterns, and brands.
- **⚡ Manufacturer Filters**: Dedicated quick-access tabs for Bridgestone, Firestone, Apollo, JK, Goodyear, and Ceat.
- **📱 Mobile-First Design**: Optimized for use on smartphones and tablets, allowing staff to check prices directly on the shop floor.
- **🎨 Premium Aesthetics**: Custom "Dark Intelligence" theme featuring Glassmorphism, Outfit typography, and glowing mint-green accents.
- **📂 Decoupled Architecture**: Data is separated from code via a centralized `tyres.json` file, making updates instant and risk-free.

---

## 🛠️ Tech Stack

- **Frontend**: Angular (Standalone Components, Signals API)
- **Styling**: Tailwind CSS v4 (with custom glassmorphism and automotive-grade dark palette)
- **Data**: Static JSON-based Intelligence Engine
- **Hosting**: Optimized for Vercel / Netlify / Static Hosting

---

## 🚦 Getting Started

### Prerequisites
- Node.js (Latest LTS recommended)
- npm

### Local Development

1. **Navigate to the dashboard directory**:
   ```powershell
   cd tyre-dashboard
   ```

2. **Install dependencies**:
   ```powershell
   npm install
   ```

3. **Start the development server**:
   ```powershell
   npm start
   ```
   The app will be available at `http://localhost:4200`.

---

## 📊 Data Management

The application's intelligence is powered by the `public/tyres.json` file. 

### To Update Prices:
1. Open `tyre-dashboard/public/tyres.json`.
2. Modify the `Consumer Price` or `MRP` fields.
3. Save the file. The dashboard will update automatically.

*Note: The original `app.py` (Streamlit version) has been kept for legacy reference but all active development is now on the Angular dashboard.*

---

## 🏗️ Repository Structure

```text
.
├── tyre-dashboard/          # Primary Angular Application
│   ├── src/                 # Source Code
│   ├── public/              # Static Assets (Logo, Data)
│   │   ├── tyres.json       # MASTER DATA SOURCE
│   │   └── logo.png         # Brand Logo
│   └── tailwind.config.js   # Style Configuration
├── tyres.json               # Root backup of the dataset
└── app.py                   # Legacy Streamlit prototype
```

---

## 🛡️ License
Internal Use Only - MOTO FINEZ.
