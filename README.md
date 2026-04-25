# MotoFinz - Price Tracker

A professional, high-performance web dashboard for managing and viewing tyre prices. Built with Angular and high-end Vanilla CSS for a premium, dark-themed experience.

## 🚀 Key Features

-   **Cloud-Synchronized Data**: Powered by **Vercel KV**, ensuring prices are consistent and persistent across every browser and device in the shop.
-   **High-Density Inventory UI**: Optimized for professional use with a compact table layout, allowing for fast scanning and data entry.
-   **Multi-Spec Dimension Filtering**: Intelligent parsing of tyre sizes into searchable components:
    -   Section Width
    -   Aspect Ratio
    -   Construction Type
    -   Wheel/Rim Diameter
    -   Load & Speed Index
-   **Role-Based Access Control**:
    -   **Admin**: Full editing capabilities and database management.
    -   **Viewer**: Read-only access for staff members.
-   **Inventory Expansion**: Integrated "Add Product" module for administrators to initialize new tyre specifications with automatic dimension parsing.
-   **Premium Aesthetics**: Dark mode "Intelligence" theme with clean, no-spinner numeric inputs and smooth micro-animations.

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
*Note: To test cloud features locally, use `vercel dev` instead of `npm start`.*

### Building for Production
```bash
npm run build
```

## 📝 Admin Instructions

1.  **Cloud Setup**: Connect a **Vercel KV** instance to your project via the Vercel Dashboard to enable global price persistence.
2.  **Adding Products**: Click **+ Add Product** to open the expansion module. Enter the manufacturer, pattern, and full tyre size (e.g., `205 55 R16`). The system will automatically parse the specs for filtering.
3.  **Editing**: Click the 📝 icon on any row to enter high-speed edit mode. Click ✔️ to save directly to the cloud.
4.  **Filtering**: Use the **Spec Grid** in the header to drill down into specific tyre dimensions (e.g., all 15-inch Bridgestones).
5.  **Exporting**: Use the **Download** icon in the header to download the current state of the global price list for offline backup.

---
© 2026 MOTO FINEZ Intelligence Systems
