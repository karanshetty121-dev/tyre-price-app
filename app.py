import streamlit as st
import pandas as pd

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

    search = st.text_input("🔍 Global Search:", placeholder="Enter Size (e.g. 145 80 12), Pattern, or Code...")

    # --- FULL DATA EXTRACTION ---

    # 1. BRIDGESTONE BSID (Passenger)
    bsid_data = {
        "Rim": ["12", "12", "12", "12", "13", "13", "14", "14", "14", "14", "15", "15", "15", "15", "15"],
        "Tyre Size": ["135 70 R12 65T", "145 70 R12 695", "145 80 R12 74H", "155 65 R12 71T", "145 70 R13 71T", "155 80 R13 79T", "155 65 R14 75T", "165 70 R14 81T", "175 65 R14 82T", "185 70 R14 88T", "175 60 R15 81H", "185 60 R15 84T", "185 65 R15 88H", "195 60 R15 88T", "205 65 R15 94H"],
        "Pattern": ["Sturdo", "EP100", "ER60", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "ER60"],
        "Type": ["TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL"],
        "Product code": ["-"] * 15,
        "Consumer Price": [2850, 3300, 3550, 3500, 3800, 4450, 4150, 4100, 5850, 5650, 6800, 6200, 6550, 7150, 7750],
        "MRP": [3061, 3544, 3825, 3776, 4089, 4789, 4470, 4421, 6313, 6066, 7296, 6651, 7028, 7690, 8355]
    }

    # 2. BRIDGESTONE TURANZA 6i
    turanza_data = {
        "Rim": ["14", "14", "15", "15", "16", "16", "17", "17", "18", "19", "20"],
        "Tyre Size": ["165 65 R14 79H", "185 70 R14 88T", "175 65 R15 84T", "195 65 R15 91V", "195 60 R16 93V", "215 60 R16 99V", "215 55 R17 94W", "225 60 R17 99V", "235 60 R18 107W", "255 55 R19 111Y", "275 45 R20 110Y"],
        "Pattern": ["Turanza 6i"] * 11,
        "Type": ["TL"] * 11,
        "Product code": ["PSR0D864", "PSR0D871", "PSR0D869", "PSR0D679", "PSROD010", "PSR0D996", "PSR0D994", "PSR0D997", "PSR0D880", "PSR0D881", "PSR0D882"],
        "Consumer Price": [5350, 6050, 6500, 7550, 8800, 9300, 12400, 12150, 15850, 21200, 27500],
        "MRP": [5869, 6643, 7141, 8301, 9749, 10212, 13695, 13417, 17290, 22692, 29447]
    }

    # 3. BRIDGESTONE DUELER (A/T002)
    dueler_data = {
        "Rim": ["15", "16", "17", "17", "18", "18", "18"],
        "Tyre Size": ["215 75 R15 100T", "235 70 R16 106T", "235 65 R17 108H", "265 65 R17 112T", "235 60 R18 107H", "265 60 R18 114H", "285 60 R18 116H"],
        "Pattern": ["Dueler A/T002"] * 7,
        "Type": ["TL"] * 7,
        "Product code": ["PSR0D860", "PSR0D849", "PSR0D859", "PSR0D848", "PSR0D851", "PSR0D852", "PSR0D896"],
        "Consumer Price": [7950, 9850, 14450, 14900, 15750, 19350, 20600],
        "MRP": [8720, 10714, 15706, 16205, 17153, 21084, 22036]
    }

    # 4. BRIDGESTONE LT (Commercial)
    lt_data = {
        "Rim": ["12", "13", "14", "15", "15"],
        "Tyre Size": ["145 R12", "155 R13", "165 R14", "195 R15", "215 75 R15"],
        "Pattern": ["Duravis R400"] * 5,
        "Type": ["TL"] * 5,
        "Product code": ["LVR0D108", "LVR0D113", "LVR0D109", "LVR0D107", "LVR0D112"],
        "Consumer Price": [3400, 4250, 4850, 6750, 7200],
        "MRP": [3641, 4574, 5123, 7283, 7746]
    }

    # 5. YOKOHAMA (Formatted Size)
    yokohama_data = {
        "Rim": ["12", "13", "13", "14", "14", "15", "15", "15", "16", "16", "17", "18", "19", "20"],
        "Tyre Size": ["145 80 R12", "145 80 R13", "155 80 R13", "165 70 R14", "175 65 R14", "175 65 R15", "185 65 R15", "195 65 R15", "195 60 R16", "205 55 R16", "215 55 R17", "235 60 R18", "255 50 R19", "275 45 R20"],
        "Pattern": ["Earth-1 Max"] * 11 + ["RV02", "G057", "G057"],
        "Type": ["TL"] * 14,
        "Product code": ["$1454", "$1155", "$1156", "$1159", "S1166", "S1169", "$1170", "$1171", "$1191", "S1181", "S1186", "R8497", "R9466", "R9470"],
        "Consumer Price": [3130, 3660, 4340, 4130, 5570, 5860, 6210, 6940, 8130, 9100, 11620, 16000, 20430, 26190],
        "MRP": [3440, 4020, 4770, 4550, 6120, 6440, 6830, 7630, 8940, 10010, 12780, 17600, 22480, 28800]
    }

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

    show_brand_table("Bridgestone Passenger (BSID)", bsid_data)
    show_brand_table("Bridgestone Premium (Turanza 6i)", turanza_data)
    show_brand_table("Bridgestone SUV (Dueler AT002)", dueler_data)
    show_brand_table("Bridgestone Commercial (Duravis)", lt_data)
    show_brand_table("Yokohama India (Earth-1 Max & Others)", yokohama_data)
