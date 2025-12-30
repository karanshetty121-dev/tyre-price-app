import streamlit as st
import pandas as pd

# 1. Standard Page Configuration
st.set_page_config(page_title="Master Data - Tyre Price List", layout="wide")

# 2. Main Title
st.title("Tyres Price List")
st.caption("Master Data • Bridgestone & Yokohama • Effective 22nd Sep 2025")

# 3. Password Protection
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if not st.session_state["password_correct"]:
        pwd = st.text_input("Enter Password:", type="password")
        if st.button("Unlock Master Data"):
            if pwd == st.secrets["password"]:
                st.session_state["password_correct"] = True
                st.rerun()
            else: st.error("❌ Incorrect password")
        return False
    return True

if check_password():
    # Standard Search Bar
    search = st.text_input("🔍 Global Search (Size or Pattern):", placeholder="Enter size or pattern (e.g. 145 80 12 or Earth-1)...")

    # --- BALANCED BRIDGESTONE DATA ---
    bridgestone_master = {
        "Brand": ["Bridgestone"] * 21,
        "Pattern": ["Sturdo", "EP100", "S322", "ER60", "248", "S248", "Sturdo", "Sturdo", "G3", "EP150", "Sturdo", "Sturdo", "Sturdo", "EP150", "Sturdo", "EP150", "Sturdo", "L607", "MY02", "Sturdo", "MY02"],
        "Tyre Size": ["135 70 R12 65T", "145 70 R12 69S", "145 70 R12 695", "145 80 R12 74H", "145 80 R12 74S", "145 80 R12 745", "145 80 R12 74T", "155 65 R12 71T", "165 60 R12 71H", "145 70 R13 071T", "145 70 R13 71T", "145 80 R13 75T", "155 65 R13 73T", "155 70 R13 075T", "155 70 R13 75T", "155 80 R13 079T", "155 80 R13 79T", "155 R13 LT 90 89Q", "165 60 R13 73H", "165 65 R13 77T", "175 60 R13 77H"],
        "Type": ["TL"] * 21,
        "Consumer Price (YRP)": [2850, 3300, 3200, 3550, 3550, 3050, 3450, 3500, 4050, 3650, 3800, 3800, 4000, 4000, 4150, 4300, 4450, 4450, 4500, 4200, 4850],
        "MRP": [3061, 3544, 3450, 3825, 3783, 3293, 3685, 3776, 4322, 3940, 4089, 4080, 4274, 4296, 4452, 4623, 4789, 4801, 4820, 4520, 5234]
    }

    # --- BALANCED YOKOHAMA DATA (FULL LIST FROM PDF) ---
    yokohama_master = {
        "Brand": ["Yokohama"] * 21,
        "Pattern": ["Earth-1 Max"] * 14 + ["GT Max", "Earth-1 Max", "AS01", "Earth-1 Max", "Earth-1 Max", "GT Max", "Earth-1 Max"],
        "Tyre Size": [
            "145 80 R12 74T", "145 80 R13 75S", "155 65 R13 73T", "155 70 R13 75T", "155 80 R13 79T", "165 65 R13 77T", "175 60 R13 77H", "175 70 R13 82H", "155 65 R14 75H", "165 65 R14 79T", "165 70 R14 81T", "165 80 R14 85T", "175 65 R14 82H", "175 70 R14 84T", "175 70 R14 84H", "185 60 R14 82H", "185 60 R14 82H", "185 65 R14 86H", "185 70 R14 88H", "185 70 R14 88H", "195 60 R14 86H"
        ],
        "Type": ["TL"] * 21,
        "Consumer Price (YRP)": [3130, 3660, 3890, 4020, 4340, 4070, 4680, 5120, 3970, 4790, 4130, 4420, 5570, 5530, 5630, 5400, 6200, 5850, 5400, 6040, 6030],
        "MRP": [3130, 3660, 3890, 4020, 4340, 4070, 4680, 5120, 3970, 4790, 4130, 4420, 5570, 5530, 5630, 5400, 6200, 5850, 5400, 6040, 6030]
    }

    # --- DISPLAY LOGIC ---
    def display_table(title, data_dict):
        df = pd.DataFrame(data_dict)
        if search:
            mask = (df["Tyre Size"].str.contains(search, case=False)) | (df["Pattern"].str.contains(search, case=False))
            filt = df[mask]
        else: filt = df
        
        if not filt.empty:
            st.subheader(f"🏷️ {title}")
            st.dataframe(filt, use_container_width=True, hide_index=True, 
                column_config={
                    "Pattern": st.column_config.Column(width="medium"),
                    "Consumer Price (YRP)": st.column_config.NumberColumn("Price (₹)", format="₹%d"),
                    "MRP": st.column_config.NumberColumn("MRP (₹)", format="₹%d")
                })
            st.markdown("---")

    display_table("Bridgestone Master List", bridgestone_master)
    display_table("Yokohama Master List", yokohama_master)
