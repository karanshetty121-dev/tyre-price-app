# Moto Finez - Master Price Intelligence Dashboard

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
-   **Premium Aesthetics**: Dark mode "Intelligence" theme with smooth micro-animations.

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
2.  **Editing**: Click the 📝 icon on any row to enter high-speed edit mode. Click ✔️ to save directly to the cloud.
3.  **Filtering**: Use the **Spec Grid** in the header to drill down into specific tyre dimensions (e.g., all 15-inch Bridgestones).
4.  **Reseting**: Use the **Reset Overrides** button to revert the cloud database to the master `tyres.json` file state.

---
© 2026 MOTO FINEZ Intelligence Systems
