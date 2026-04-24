# Moto Finez - Master Price Intelligence Dashboard

A professional, high-performance web dashboard for managing and viewing tyre prices. Built with Angular and high-end Vanilla CSS for a premium, dark-themed experience.

## 🚀 Key Features

-   **Role-Based Access Control**: Separate accounts for administrators and viewers.
-   **Live Inventory Catalog**: Real-time filtering by brand and search queries.
-   **Price Intelligence**: Instant access to Consumer Prices and MRP.
-   **Admin Editing Suite**:
    -   Inline price editing for Consumer Price and MRP.
    -   Persistent local storage overrides.
    -   Data Export (JSON) for master file updates.
    -   Global reset to revert changes to the master file state.
-   **Premium UI/UX**: Dark mode aesthetic, responsive design, and smooth micro-animations.

## 🔑 Authentication

| Role | Username | Password |
| :--- | :--- | :--- |
| **Administrator** | `karanshetty` | `Shetty@1992!` |
| **Viewer** | `motofinez` | `moto2026` |

## 🛠️ Getting Started

### Development Server
To start a local development server:
```bash
npm install
npm start
```
Navigate to `http://localhost:4200/`.

### Building for Production
```bash
npm run build
```
The build artifacts will be stored in the `dist/` directory.

## 📂 Project Structure

- `src/app/`: Core application logic and styling.
- `public/tyres.json`: The master dataset of tyre prices.
- `public/logo.png`: Brand identity assets.

## 📝 Admin Instructions

1. **Editing**: Click the 📝 icon on any row to enter edit mode. Click ✔️ to save or ❌ to cancel.
2. **Exporting**: Click **Export JSON** to download the modified dataset. This file can be used to update `public/tyres.json` permanently.
3. **Resetting**: Click **Reset Overrides** to clear all browser-saved changes and return to the master price list.

---
© 2026 MOTO FINEZ Intelligence Systems
