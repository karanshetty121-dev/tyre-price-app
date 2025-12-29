import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Tyre Price Finder", layout="wide")

# 2. Password Protection
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if not st.session_state["password_correct"]:
        st.title("🔐 Locked Dashboard")
        pwd = st.text_input("Enter Password:", type="password")
        if st.button("Unlock"):
            if pwd == st.secrets["password"]:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Incorrect password")
        return False
    return True

if check_password():
    st.title("🛞 Multi-Brand Tyre Price List")
    st.caption("Effective From: 22nd September 2025")

    # Logout Button
    if st.sidebar.button("Log Out"):
        st.session_state["password_correct"] = False
        st.rerun()

    # --- BRAND DATA SECTION ---
    
    # Bridgestone Data (Extracted from your PDFs)
    bridgestone_data = {
        "Rim": ["12", "14", "15", "16", "17"],
        "Tyre Size": ["145 R12", "165 65 R14 79H", "215 75 R15 100T", "235 70 R16 106T", "235 65 R17 108H"],
        "Pattern": ["Duravis R400", "Turanza 6i", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002"],
        "Type": ["TL", "TL", "TL", "TL", "TL"],
        "Product code": ["LVR0D108", "PSR0D864", "PSR0D860", "PSR0D849", "PSR0D859"],
        "Consumer Price": [3400, 5350, 7950, 9850, 14450],
        "MRP": [3641, 5869, 8720, 10714, 15706]
    }

    # Yokohama Data (Extracted from your PDF)
    yokohama_data = {
        "Rim": ["12", "13", "13", "14", "15"],
        "Tyre Size": ["145/80 R12", "145/80 R13", "155/65 R13", "165/70 R14", "175/65 R15"],
        "Pattern": ["Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max"],
        "Type": ["TL", "TL", "TL", "TL", "TL"],
        "Product code": ["$1454", "$1155", "S1163", "$1159", "S1169"],
        "Consumer Price": [3130, 3660, 3890, 4130, 5860],
        "MRP": [3440, 4020, 4270, 4550, 6440]
    }

    # --- SEARCH & DISPLAY LOGIC ---
    search = st.text_input("🔍 Global Search:", placeholder="Search Size, Pattern, or Product Code...")

    def display_brand_table(brand_name, data_dict):
        df = pd.DataFrame(data_dict)
        
        # Filtering logic
        if search:
            mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
            filt = df[mask]
        else:
            filt = df
        
        if not filt.empty:
            st.header(f"🏷️ {brand_name}")
            st.dataframe(
                filt,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Consumer Price": st.column_config.NumberColumn("Consumer Price", format="₹%d"),
                    "MRP": st.column_config.NumberColumn("MRP", format="₹%d"),
                }
            )
            st.write("---") # Creates the visual gap between brands

    # Display the tables
    [span_0](start_span)[span_1](start_span)[span_2](start_span)display_brand_table("Bridgestone", bridgestone_data)[span_0](end_span)[span_1](end_span)[span_2](end_span)
    [span_3](start_span)display_brand_table("Yokohama", yokohama_data)[span_3](end_span)
