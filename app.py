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

    # --- BALANCED DATA LISTS ---
    
    # Bridgestone Passenger (Turanza 6i & BSID)
    BRIDGESTONE_PASSENGER = {
        "Rim": ["12", "12", "12", "13", "13", "14", "14", "14", "15", "15", "15", "15", "15", "15", "16", "16", "16", "16", "16", "16", "16", "17", "17", "17", "17", "17", "18", "18", "18", "18", "18", "19", "19", "20", "20"],
        "Tyre Size": ["135 70 R12 65T", "145 80 R12 74T", "155 65 R12 71T", "145 70 R13 71T", "155 80 R13 79T", "165 65 R14 79H", "175 65 R14 82T", "185 70 R14 88T", "175 65 R15 84T", "185 60 R15 84T", "185 65 R15 88H", "185 70 R15 89H", "195 55 R15 85V", "195 65 R15 91V", "185 55 R16 83V", "195 55 R16 87H", "195 60 R16 93V", "205 55 R16 91W", "205 60 R16 92V", "215 60 R16 99V", "225 60 R16 102W", "205 55 R17 91H", "215 55 R17 94W", "225 50 R17 98Y", "225 60 R17 99V", "235 55 R17 103W", "215 55 R18 95V", "235 60 R18 107W", "245 45 R18 100Y", "255 55 R18 109W", "265 60 R18 110H", "235 55 R19 101W", "255 50 R19 107W", "255 55 R20 110W", "275 45 R20 110Y"],
        "Pattern": ["Sturdo", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Dueler D684", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i"],
        "Type": ["TL"] * 35,
        "Product code": ["-", "-", "-", "-", "-", "PSR0D864", "PSR0D868", "PSR0D871", "PSR0D869", "PSR0D870", "PSR0D865", "PSR0D890", "PSR0D872", "PSR0D679", "PSR0D678", "PSR0D866", "PSROD010", "PSR0D874", "PSR0D877", "PSR0D996", "PSR0D009", "PSR0D876", "PSR0D994", "PSR0D893", "PSR0D997", "PSR0D878", "PSR0D854", "PSR0D880", "PSR0D894", "PSR0D886", "LVR0D112", "PSR0D863", "PSR0D884", "PSR0D887", "PSR0D882"],
        "Consumer Price": [2850, 3450, 3500, 3800, 4450, 5350, 6200, 6050, 6500, 6500, 6850, 6650, 6900, 7550, 8450, 9250, 8800, 10350, 8550, 9300, 10300, 10000, 12400, 12650, 12150, 14600, 13400, 15850, 16100, 19700, 18700, 19650, 21650, 25450, 27500],
        "MRP": [3061, 3685, 3776, 4089, 4789, 5869, 6826, 6643, 7141, 7127, 7508, 7256, 7580, 8301, 9294, 10083, 9749, 11286, 9291, 10212, 11284, 10898, 13695, 13946, 13417, 15934, 14620, 17290, 17670, 21448, 20006, 21010, 23207, 27210, 29447]
    }

    # Bridgestone SUV (Dueler All-Terrain A/T002)
    BRIDGESTONE_DUELER = {
        "Rim": ["15", "16", "17", "17", "17", "18", "18", "18", "18", "18"],
        "Tyre Size": ["215 75 R15 100T", "235 70 R16 106T", "235 65 R17 108H", "245 60 R17 108H", "265 65 R17 112T", "235 60 R18 107H", "245 55 R18 103V", "255 65 R18 111H", "265 60 R18 114H", "285 60 R18 116H"],
        "Pattern": ["Dueler A/T002"] * 10,
        "Type": ["TL"] * 10,
        "Product code": ["PSR0D860", "PSR0D849", "PSR0D859", "PSR0D858", "PSR0D848", "PSR0D851", "PSR0D850", "PSR0D853", "PSR0D852", "PSR0D896"],
        "Consumer Price": [7950, 9850, 14450, 15000, 14900, 15750, 16550, 13100, 19350, 20600],
        "MRP": [8720, 10714, 15706, 16081, 16205, 17153, 17702, 14254, 21084, 22036]
    }

    # Bridgestone Commercial (Duravis LT)
    BRIDGESTONE_LT = {
        "Rim": ["12", "13", "14", "14", "15", "15", "15"],
        "Tyre Size": ["145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"],
        "Pattern": ["Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400 Plus"],
        "Type": ["TL", "TL", "TL", "TL", "TL", "TL", "TT"],
        "Product code": ["LVR0D108", "LVR0D113", "LVR0D109", "LVROD106", "LVR0D107", "LVR0D112", "LSR0D004"],
        "Consumer Price": [3400, 4250, 4850, 5800, 6750, 7200, 9650],
        "MRP": [3641, 4574, 5123, 6260, 7283, 7746, 10412]
    }

    # Yokohama India (Earth-1 Max & Others)
    YOKOHAMA_DATA = {
        "Rim": ["12", "13", "13", "13", "13", "13", "14", "14", "14", "15", "15", "15", "15", "16", "16", "17", "18", "19", "20"],
        "Tyre Size": ["145/80 R12", "145/80 R13", "155/65 R13", "155/80 R13", "175/60 R13", "175/70 R13", "165/70 R14", "175/65 R14", "185/70 R14", "175/65 R15", "185/65 R15", "195/60 R15", "215/75 R15", "195/60 R16", "205/65 R16", "215/55 R17", "235/60 R18", "255/50 R19", "275/45 R20"],
        "Pattern": ["Earth-1 Max"] * 12 + ["G015", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "RV02", "G057", "G057"],
        "Type": ["TL"] * 19,
        "Product code": ["$1454", "$1155", "S1163", "$1156", "S1173", "$1158", "$1159", "S1166", "S1161", "S1169", "$1170", "$1177", "R5880", "$1191", "S1184", "S1186", "R8497", "R9466", "R9470"],
        "Consumer Price": [3130, 3660, 3890, 4340, 4680, 5120, 4130, 5570, 5400, 5860, 6210, 6770, 7180, 8130, 7530, 11620, 16000, 20430, 26190],
        "MRP": [3440, 4020, 4270, 4770, 5150, 5630, 4550, 6120, 5940, 6440, 6830, 7440, 7900, 8940, 8280, 12780, 17600, 22480, 28800]
    }

    # --- SEARCH & DISPLAY LOGIC ---
    search = st.text_input("🔍 Global Search:", placeholder="Search by Size, Brand, or Product Code...")

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

    show_brand_table("Bridgestone Passenger (Turanza 6i & BSID)", BRIDGESTONE_PASSENGER)
    show_brand_table("Bridgestone SUV (Dueler A/T002)", BRIDGESTONE_DUELER)
    show_brand_table("Bridgestone Commercial (Duravis R400)", BRIDGESTONE_LT)
    show_brand_table("Yokohama India (Earth-1 Max & Others)", YOKOHAMA_DATA)
