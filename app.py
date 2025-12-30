import streamlit as st
import pandas as pd

# 1. Page Configuration
st.set_page_config(page_title="MOTO FINEZ - Master Data", layout="wide")

# Custom Branding CSS
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; margin-top: -20px; }
    .sub-heading { font-size: 14px; color: gray; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 2. Header Section: Logo & Titles
col1, col2 = st.columns([1, 4])
with col1:
    # Company Logo Placeholder
    st.image("https://via.placeholder.com/150x150.png?text=MOTO+FINEZ", width=120) 
with col2:
    st.markdown('<div class="main-title">Tyres Price List</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-heading">Master Data - Bridgestone India (Effective 22nd Sep 2025)</div>', unsafe_allow_html=True)

# 3. Password Protection
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if not st.session_state["password_correct"]:
        st.title("🔐 Access Required")
        pwd = st.text_input("Enter MOTO FINEZ Credentials:", type="password")
        if st.button("Access Master Data"):
            if pwd == st.secrets["password"]:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Invalid Password")
        return False
    return True

if check_password():
    if st.sidebar.button("Logout"):
        st.session_state["password_correct"] = False
        st.rerun()

    search = st.text_input("🔍 Global Search:", placeholder="Enter Size (e.g. 145 80 12), Brand, or Pattern...")

    # --- THE COMPLETE BRIDGESTONE MASTER DATASET (90+ ENTRIES) ---
    bridgestone_master = {
        "Rim": [
            "12", "13", "14", "15", "15", "16", "17", "17", "18", "18", "19", "19", "20", "21", "16", "17", "18", "19", "20", "21", 
            "14", "14", "14", "15", "15", "15", "15", "15", "15", "15", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", "16", 
            "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "18", "18", "18", "18", "18", "18", "18", 
            "19", "19", "19", "19", "19", "19", "20", "20", "20", "20", "20", "15", "16", "17", "17", "17", "18", "18", "18", "18", "18", 
            "12", "13", "14", "14", "15", "15", "15"
        ],
        "Tyre Size": [
            "145 80 R12 745", "155 80 R13 079T", "165 80 R14 85T", "185 65 R15 88H", "215 75 R15 1065", "215 55 R16 93V", "215 45 R17 91Y", "235 65 R17 104H", "235 50 R18 101W", "255 55 R18 109W", "245 45 R19 98Y", "275 40 R19 105Y", "275 35 R20 102Y", "235 50 R21 101W", 
            "225 50 R16 92W", "225 50 R17 94W", "245 40 R18 93Y", "275 35 R19 96W", "245 45 R20 99Y", "275 35 R21 99Y", 
            "165 65 R14 79H", "175 65 R14 82T", "185 70 R14 88T", "175 65 R15 84T", "185 60 R15 84T", "185 65 R15 88H", "185 70 R15 89H", "195 55 R15 85V", "195 65 R15 91V", "205 55 R15 88V", "185 55 R16 83V", "185 60 R16 86H", "195 55 R16 87H", "195 60 R16 93V", "205 50 R16 87V", "205 55 R16 91W", "205 60 R16 92V", "205 65 R16 95H", "215 55 R16 97W", "215 60 R16 99V", "215 65 R16 98V", "225 50 R16 92W", "225 55 R16 99Y", "225 60 R16 102W", 
            "205 45 R17 88Y", "205 55 R17 91H", "215 45 R17 91W", "215 55 R17 94W", "225 45 R17 94W", "225 50 R17 98Y", "225 55 R17 101W", "225 60 R17 99V", "235 55 R17 103W", "235 60 R17 102V", "245 45 R17 99W", 
            "215 55 R18 95V", "235 45 R18 98W", "235 50 R18 97W", "235 60 R18 107W", "235 65 R18 106V", "245 45 R18 100Y", "255 55 R18 109W", 
            "235 55 R19 101W", "255 50 R19 107W", "255 55 R19 111Y", "265 50 R19 110W", "275 55 R19 111V", "285 45 R19 107W", 
            "255 50 R20 109W", "255 55 R20 110W", "275 45 R20 110Y", "275 50 R20 109W", "285 50 R20 116W", 
            "215 75 R15 100T", "235 70 R16 106T", "235 65 R17 108H", "245 60 R17 108H", "265 65 R17 112T", "235 60 R18 107H", "245 55 R18 103V", "255 65 R18 111H", "265 60 R18 114H", "285 60 R18 116H", 
            "145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"
        ],
        "Pattern": [
            "248", "EP150", "Sturdo", "B250", "P.Cab", "T005", "5001", "D684", "T001", "Alenza 001", "S001", "5001", "S007A", "Alenza 001", "5001", "5001", "RE050", "5001", "T005", "5001", 
            "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", 
            "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", 
            "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", "Dueler A/T002", 
            "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400 Plus"
        ],
        "Type": [
            "TT", "TL", "TL", "TL", "TT", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", 
            "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", 
            "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", 
            "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", "TL", 
            "TL", "TL", "TL", "TL", "TL", "TL", "TT"
        ],
        "Consumer Price": [
            3550, 4300, 4600, 6550, 7850, 11450, 9750, 13900, 20050, 18100, 22300, 28850, 32850, 29450, 14550, 17100, 24050, 32900, 32900, 39650, 
            5350, 6200, 6050, 6500, 6500, 6850, 6650, 6900, 7550, 7700, 8450, 7250, 9250, 8800, 9200, 10350, 8550, 8200, 11550, 9300, 10650, 12300, 11850, 10300, 
            10000, 10000, 10100, 12400, 12700, 12650, 12550, 12150, 14600, 20200, 13650, 13400, 20800, 21050, 15850, 21400, 16100, 19700, 
            19650, 21650, 21200, 26500, 25250, 28800, 25500, 25450, 27500, 25850, 27650, 7950, 9850, 14450, 15000, 14900, 15750, 16550, 13100, 19350, 20600, 
            3400, 4250, 4850, 5800, 6750, 7200, 9650
        ],
        "MRP": [
            3783, 4623, 4958, 7028, 8430, 12229, 10404, 14849, 21439, 19364, 23633, 30537, 34803, 31195, 15398, 18101, 25479, 34545, 34551, 41241, 
            5869, 6826, 6643, 7141, 7127, 7508, 7256, 7580, 8301, 8434, 9294, 7844, 10083, 9749, 10046, 11286, 9291, 8919, 12697, 10212, 11691, 13490, 13009, 11284, 
            10897, 10898, 11142, 13695, 13998, 13946, 13635, 13417, 15934, 22287, 15041, 14620, 22853, 22913, 17290, 23539, 17670, 21448, 
            21010, 23207, 22692, 28354, 26973, 30698, 27315, 27210, 29447, 27653, 30004, 8720, 10714, 15706, 16081, 16205, 17153, 17702, 14254, 21084, 22036, 
            3641, 4574, 5123, 6260, 7283, 7746, 10412
        ]
    }

    # --- RENDER TABLE ---
    df = pd.DataFrame(bridgestone_master)
    if search:
        mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
        filt = df[mask]
    else:
        filt = df

    st.subheader("📊 Master Data: Bridgestone India")
    st.dataframe(
        filt, use_container_width=True, hide_index=True,
        column_config={
            "Consumer Price": st.column_config.NumberColumn("Consumer Price (₹)", format="₹%d"),
            "MRP": st.column_config.NumberColumn("MRP (₹)", format="₹%d")
        }
    )
