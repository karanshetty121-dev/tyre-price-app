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
            # Ensure you have 'password' set in Streamlit Cloud Secrets
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

    # --- THE DATA (BALANCED LISTS) ---
    
    # [span_0](start_span)[span_1](start_span)[span_2](start_span)[span_3](start_span)[span_4](start_span)[span_5](start_span)[span_6](start_span)Data from Turanza 6i and BSID PDFs[span_0](end_span)[span_1](end_span)[span_2](end_span)[span_3](end_span)[span_4](end_span)[span_5](end_span)[span_6](end_span)
    BRIDGESTONE_PASSENGER = {
        "Rim": ["14", "14", "14", "15", "15", "15", "15", "15", "15", "15", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "18", "18", "18", "18", "18", "18", "18", "19", "19", "19", "19", "19", "19", "20", "20", "20", "20", "20"],
        "Tyre Size": ["165 65 R14 79H", "175 65 R14 82T", "185 70 R14 88T", "175 65 R15 84T", "185 60 R15 84T", "185 65 R15 88H", "185 70 R15 89H", "195 55 R15 85V", "195 65 R15 91V", "205 55 R15 88V", "185 55 R16 83V", "185 60 R16 86H", "195 55 R16 87H", "195 60 R16 93V", "205 50 R16 87V", "205 55 R16 91W", "205 60 R16 92V", "205 65 R16 95H", "215 55 R16 97W", "215 60 R16 99V", "215 65 R16 98V", "225 50 R16 92W", "225 55 R16 99Y", "225 60 R16 102W", "205 45 R17 88Y", "205 55 R17 91H", "215 45 R17 91W", "215 55 R17 94W", "225 45 R17 94W", "225 50 R17 98Y", "225 55 R17 101W", "225 60 R17 99V", "235 55 R17 103W", "235 60 R17 102V", "245 45 R17 99W", "215 55 R18 95V", "235 45 R18 98W", "235 50 R18 97W", "235 60 R18 107W", "235 65 R18 106V", "245 45 R18 100Y", "255 55 R18 109W", "235 55 R19 101W", "255 50 R19 107W", "255 55 R19 111Y", "265 50 R19 110W", "275 55 R19 111V", "285 45 R19 107W", "255 50 R20 109W", "255 55 R20 110W", "275 45 R20 110Y", "275 50 R20 109W", "285 50 R20 116W"],
        "Pattern": ["Turanza 6i"] * 53,
        "Type": ["TL"] * 53,
        "Product code": ["PSR0D864", "PSR0D868", "PSR0D871", "PSR0D869", "PSR0D870", "PSR0D865", "PSR0D890", "PSR0D872", "PSR0D679", "PSR0D875", "PSR0D678", "PSROD889", "PSR0D866", "PSROD010", "PSR0D873", "PSR0D874", "PSR0D877", "PSR0D855", "PSR0D677", "PSR0D996", "PSR0D011", "PSR0D676", "PSROD012", "PSR0D009", "PSR0D019", "PSR0D876", "PSR0D014", "PSR0D994", "PSR0D016", "PSR0D893", "PSR0D883", "PSR0D997", "PSR0D878", "PSR0D999", "PSR0D017", "PSR0D854", "PSR0D021", "PSR0D862", "PSR0D880", "PSR0D998", "PSR0D894", "PSR0D886", "PSR0D863", "PSR0D884", "PSR0D881", "PSR0D888", "PSR0D879", "PSR0D005", "PSROD885", "PSR0D887", "PSR0D882", "PSR0D861", "PSR0D992"],
        "Consumer Price": [5350, 6200, 6050, 6500, 6500, 6850, 6650, 6900, 7550, 7700, 8450, 7250, 9250, 8800, 9200, 10350, 8550, 8200, 11550, 9300, 10650, 12300, 11850, 10300, 10000, 10000, 10100, 12400, 12700, 12650, 12550, 12150, 14600, 20200, 13650, 13400, 20800, 21050, 15850, 21400, 16100, 19700, 19650, 21650, 21200, 26500, 25250, 28800, 25500, 25450, 27500, 25850, 27650],
        "MRP": [5869, 6826, 6643, 7141, 7127, 7508, 7256, 7580, 8301, 8434, 9294, 7844, 10083, 9749, 10046, 11286, 9291, 8919, 12697, 10212, 11691, 13490, 13009, 11284, 10897, 10898, 11142, 13695, 13998, 13946, 13635, 13417, 15934, 22287, 15041, 14620, 22853, 22913, 17290, 23539, 17670, 21448, 21010, 23207, 22692, 28354, 26973, 30698, 27315, 27210, 29447, 27653, 30004]
    }

    # [span_7](start_span)Data from LT PDF[span_7](end_span)
    BRIDGESTONE_LT = {
        "Rim": ["12", "13", "14", "14", "15", "15", "15"],
        "Tyre Size": ["145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"],
        "Pattern": ["Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400 Plus"],
        "Type": ["TL", "TL", "TL", "TL", "TL", "TL", "TT"],
        "Product code": ["LVR0D108", "LVR0D113", "LVR0D109", "LVROD106", "LVR0D107", "LVR0D112", "LSR0D004"],
        "Consumer Price": [3400, 4250, 4850, 5800, 6750, 7200, 9650],
        "MRP": [3641, 4574, 5123, 6260, 7283, 7746, 10412]
    }

    # [span_8](start_span)Data from Dueler AT002 PDF[span_8](end_span)
    BRIDGESTONE_DUELER = {
        "Rim": ["15", "16", "17", "17", "17", "18", "18", "18", "18", "18"],
        "Tyre Size": ["215 75 R15 100T", "235 70 R16 106T", "235 65 R17 108H", "245 60 R17 108H", "265 65 R17 112T", "235 60 R18 107H", "245 55 R18 103V", "255 65 R18 111H", "265 60 R18 114H", "285 60 R18 116H"],
        "Pattern": ["Dueler A/T002"] * 10,
        "Type": ["TL"] * 10,
        "Product code": ["PSR0D860", "PSR0D849", "PSR0D859", "PSR0D858", "PSR0D848", "PSR0D851", "PSR0D850", "PSR0D853", "PSR0D852", "PSR0D896"],
        "Consumer Price": [7950, 9850, 14450, 15000, 14900, 15750, 16550, 13100, 19350, 20600],
        "MRP": [8720, 10714, 15706, 16081, 16205, 17153, 17702, 14254, 21084, 22036]
    }

    # [span_9](start_span)Data from Yokohama PDF[span_9](end_span)
    YOKOHAMA_DATA = {
        "Rim": ["12", "13", "13", "13", "13", "13", "13", "13", "14", "14", "14", "14", "14", "14", "14", "14", "14", "14", "14", "14", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15", "15"],
        "Tyre Size": ["145/80 R12", "145/80 R13", "155/65 R13", "155/70 R13", "155/80 R13", "165/65 R13", "175/60 R13", "175/70 R13", "155/65 R14", "165/65 R14", "165/70 R14", "165/80 R14", "175/65 R14", "175/70 R14", "175/70 R14", "185/60 R14", "185/65 R14", "185/70 R14", "185/70 R14", "195/60 R14", "195/65 R14", "195/70 R14", "175/60 R15", "175/65 R15", "175/65 R15", "185/60 R15", "185/60 R15", "185/65 R15", "185/65 R15", "185/70 R15", "195/50 R15", "195/55 R15", "195/60 R15", "195/60 R15", "195/65 R15", "195/65 R15", "205/50 R15", "205/55 R15", "205/60 R15", "205/65 R15", "215/75 R15"],
        "Pattern": ["Earth-1 Max"] * 41,
        "Type": ["TL"] * 41,
        "Product code": ["$1454", "$1155", "S1163", "$1157", "$1156", "S1164", "S1173", "$1158", "$1190", "S1165", "$1159", "$1179", "S1166", "$1160", "S2221", "S1174", "$1167", "S1161", "S2201", "S1175", "S1168", "$1162", "S2222", "S1169", "S2203", "S1176", "S2223", "$1170", "S2196", "S1192", "F8948", "F8946", "S2209", "$1177", "$1171", "S2216", "F8947", "F8945", "F8940", "S1172", "R5880"],
        "Consumer Price": [3130, 3660, 3890, 4020, 4340, 4070, 4680, 5120, 3970, 4790, 4130, 4420, 5570, 5530, 5630, 5400, 5320, 5400, 5490, 6030, 5660, 6690, 6570, 5860, 5960, 5970, 6060, 6210, 6300, 6300, 7290, 6480, 6880, 6770, 6940, 7050, 8160, 7320, 7850, 7380, 7180],
        "MRP": [3440, 4020, 4270, 4420, 4770, 4480, 5150, 5630, 4370, 5270, 4550, 4860, 6120, 6090, 6190, 5940, 5850, 5940, 6040, 6640, 6220, 7360, 7230, 6440, 6550, 6560, 6670, 6830, 6940, 6930, 8020, 7130, 7570, 7440, 7630, 7750, 8980, 8060, 8630, 8120, 7900]
    }

    # --- SEARCH & DISPLAY LOGIC ---
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

    show_brand_table("Bridgestone Passenger (Turanza 6i)", BRIDGESTONE_PASSENGER)
    show_brand_table("Bridgestone SUV (Dueler AT002)", BRIDGESTONE_DUELER)
    show_brand_table("Bridgestone Commercial (Duravis)", BRIDGESTONE_LT)
    show_brand_table("Yokohama India (Earth-1 Max)", YOKOHAMA_DATA)
