import streamlit as st
import pandas as pd
from data import BRIDGESTONE_PASSENGER, BRIDGESTONE_LT, BRIDGESTONE_ALL_TERRAIN, YOKOHAMA_DATA

st.set_page_config(page_title="Tyre Price Finder", layout="wide")

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
    st.title("🛞 Complete Tyre Price Dashboard")
    st.caption("Prices effective from 22nd September 2025")

    if st.sidebar.button("Log Out"):
        st.session_state["password_correct"] = False
        st.rerun()

    search = st.text_input("🔍 Global Search:", placeholder="Enter Size, Pattern, or Code...")

    def show_brand_table(title, data_dict):
        df = pd.DataFrame(data_dict)
        if search:
            mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
            filt = df[mask]
        else:
            filt = df
        
        if not filt.empty:
            st.header(f"🏷️ {title}")
            st.dataframe(
                filt, 
                use_container_width=True, 
                hide_index=True,
                column_config={
                    "Consumer Price": st.column_config.NumberColumn("Consumer Price", format="₹%d"),
                    "MRP": st.column_config.NumberColumn("MRP", format="₹%d"),
                }
            )
            st.markdown("---")

    # Grouped display for better mobile scrolling
    show_brand_table("Bridgestone Passenger (Turanza)", BRIDGESTONE_PASSENGER)
    show_brand_table("Bridgestone Commercial (Duravis)", BRIDGESTONE_LT)
    show_brand_table("Bridgestone All-Terrain (Dueler)", BRIDGESTONE_ALL_TERRAIN)
    show_brand_table("Yokohama India (Earth-1)", YOKOHAMA_DATA)
