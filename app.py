import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="Tyre Price Finder", layout="wide")

# 2. Password Protection Logic
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

    search = st.text_input("🔍 Global Search:", placeholder="Enter Size (e.g., 145 80 12), Pattern, or Code...")

    # --- FULL DATA EXTRACTION FROM ALL PDFS AND IMAGES ---

    # Category 1: Bridgestone Passenger (BSID) - From PDF and Image 6
    bsid_data = {
        "Rim": ["12", "12", "12", "12", "12", "12", "12", "12", "13", "13", "13", "13", "13", "13", "13", "13", "14", "14", "14", "14", "14", "15", "15", "15", "15", "16", "16", "16", "16", "17", "17", "18", "18", "19", "20", "21"],
        "Tyre Size": ["135 70 R12 65T", "145 70 R12 69S", "145 80 R12 74H", "145 80 R12 74S", "155 65 R12 71T", "165 60 R12 71H", "145 70 R13 71T", "145 80 R13 75T", "155 65 R13 73T", "155 70 R13 75T", "155 80 R13 79T", "165 60 R13 73H", "165 65 R13 77T", "175 70 R13 82T", "155 65 R14 75T", "165 70 R14 81T", "165 80 R14 85T", "175 65 R14 82T", "185 65 R14 86T", "175 60 R15 81H", "185 60 R15 84T", "185 65 R15 88H", "195 65 R15 91V", "185 55 R16 83H", "195 55 R16 87V", "205 60 R16 92H", "215 60 R16 95H", "205 50 R17 93H", "215 55 R17 94V", "225 55 R18 98V", "235 55 R18 100V", "245 45 R19 98Y", "265 55 R20 113V", "235 50 R21 101W"],
        "Pattern": ["Sturdo", "EP100", "ER60", "S248", "Sturdo", "G3", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "MY02", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "EP150", "B250", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "EP150", "EP150", "G3", "T001", "EP150", "T005A", "T001", "D684", "S001", "D693", "Alenza 001"],
        "Type": ["TL"] * 34,
        "Product code": ["-"] * 34,
        "Consumer Price": [2850, 3300, 3550, 3050, 3500, 4050, 3800, 3800, 4000, 4150, 4450, 4500, 4200, 5300, 4150, 4100, 4350, 5850, 5550, 6800, 6200, 6550, 7250, 8000, 8400, 8500, 8950, 10450, 12200, 15200, 20800, 22300, 27900, 29450],
        "MRP": [3061, 3544, 3825, 3293, 3776, 4322, 4089, 4080, 4274, 4452, 4789, 4820, 4520, 5694, 4470, 4421, 4652, 6312, 5970, 7296, 6651, 7028, 7795, 8530, 8968, 9068, 9555, 11180, 13043, 16224, 22217, 23633, 29533, 31195]
    }

    # Category 2: Bridgestone Turanza 6i - From Turanza PDF
    turanza_data = {
        "Rim": ["14", "14", "15", "15", "15", "15", "16", "16", "16", "17", "17", "18", "18", "19", "20"],
        "Tyre Size": ["165 65 R14 79H", "185 70 R14 88T", "175 65 R15 84T", "185 65 R15 88H", "195 55 R15 85V", "195 65 R15 91V", "195 55 R16 87H", "205 60 R16 92V", "215 60 R16 99V", "215 55 R17 94W", "225 60 R17 99V", "235 60 R18 107W", "245 45 R18 100Y", "255 55 R19 111Y", "275 45 R20 110Y"],
        "Pattern": ["Turanza 6i"] * 15,
        "Type": ["TL"] * 15,
        "Product code": ["PSR0D864", "PSR0D871", "PSR0D869", "PSR0D865", "PSR0D872", "PSR0D679", "PSR0D866", "PSR0D877", "PSR0D996", "PSR0D994", "PSR0D997", "PSR0D880", "PSR0D894", "PSR0D881", "PSR0D882"],
        "Consumer Price": [5350, 6050, 6500, 6850, 6900, 7550, 9250, 8550, 9300, 12400, 12150, 15850, 16100, 21200, 27500],
        "MRP": [5869, 6643, 7141, 7508, 7580, 8301, 10083, 9291, 10212, 13695, 13417, 17290, 17670, 22692, 29447]
    }

    # Category 3: Bridgestone Dueler (A/T002) - From Dueler PDF
    dueler_data = {
        "Rim": ["15", "16", "17", "17", "17", "18", "18", "18", "18", "18"],
        "Tyre Size": ["215 75 R15 100T", "235 70 R16 106T", "235 65 R17 108H", "245 60 R17 108H", "265 65 R17 112T", "235 60 R18 107H", "245 55 R18 103V", "255 65 R18 111H", "265 60 R18 114H", "285 60 R18 116H"],
        "Pattern": ["Dueler A/T002"] * 10,
        "Type": ["TL"] * 10,
        "Product code": ["PSR0D860", "PSR0D849", "PSR0D859", "PSR0D858", "PSR0D848", "PSR0D851", "PSR0D850", "PSR0D853", "PSR0D852", "PSR0D896"],
        "Consumer Price": [7950, 9850, 14450, 15000, 14900, 15750, 16550, 13100, 19350, 20600],
        "MRP": [8720, 10714, 15706, 16081, 16205, 17153, 17702, 14254, 21084, 22036]
    }

    # Category 4: Bridgestone LT (Commercial) - From LT PDF
    lt_data = {
        "Rim": ["12", "13", "14", "14", "15", "15", "15"],
        "Tyre Size": ["145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"],
        "Pattern": ["Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400 Plus"],
        "Type": ["TL", "TL", "TL", "TL", "TL", "TL", "TT"],
        "Product code": ["LVR0D108", "LVR0D113", "LVR0D109", "LVROD106", "LVR0D107", "LVR0D112", "LSR0D004"],
        "Consumer Price": [3400, 4250, 4850, 5800, 6750, 7200, 9650],
        "MRP": [3641, 4574, 5123, 6260, 7283, 7746, 10412]
    }

    # Category 5: Yokohama (Full List with Formatted Size) - From Yokohama PDF
    yokohama_data = {
        "Rim": ["12", "13", "13", "13", "13", "13", "13", "14", "14", "14", "14", "14", "14", "14", "14", "14", "15", "15", "15", "15", "15", "15", "15", "15", "16", "16", "16", "16", "17", "17", "18", "19", "20", "21"],
        "Tyre Size": ["145 80 R12", "145 80 R13", "155 65 R13", "155 70 R13", "155 80 R13", "165 65 R13", "175 70 R13", "155 65 R14", "165 65 R14", "165 70 R14", "165 80 R14", "175 65 R14", "175 70 R14", "185 60 R14", "185 70 R14", "195 60 R14", "175 60 R15", "175 65 R15", "185 60 R15", "185 65 R15", "185 70 R15", "195 55 R15", "195 65 R15", "215 75 R15", "185 60 R16", "195 55 R16", "205 60 R16", "215 60 R16", "215 55 R17", "225 45 R17", "235 60 R18", "255 50 R19", "275 45 R20", "295 35 R21"],
        "Pattern": ["Earth-1 Max"] * 29 + ["GT Max", "RV02", "G057", "G057", "V105"],
        "Type": ["TL"] * 34,
        "Product code": ["$1454", "$1155", "S1163", "$1157", "$1156", "S1164", "$1158", "$1190", "S1165", "$1159", "$1179", "S1166", "$1160", "S1174", "S1161", "S1175", "S2222", "S1169", "S1176", "$1170", "S1192", "F8946", "$1171", "R5880", "S1193", "$1180", "S1182", "S1185", "S1186", "S2202", "R8497", "R9466", "R9470", "F8199"],
        "Consumer Price": [3130, 3660, 3890, 4020, 4340, 4070, 5120, 3970, 4790, 4130, 4420, 5570, 5530, 5400, 5400, 6030, 6570, 5860, 5970, 6210, 6300, 6480, 6940, 7180, 6760, 8340, 7750, 8450, 11620, 11630, 16000, 20430, 26190, 34110],
        "MRP": [3440, 4020, 4270, 4420, 4770, 4480, 5630, 4370, 5270, 4550, 4860, 6120, 6090, 5940, 5940, 6640, 7230, 6440, 6560, 6830, 6930, 7130, 7630, 7900, 7440, 9180, 8530, 9300, 12780, 12800, 17600, 22480, 28800, 37520]
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
