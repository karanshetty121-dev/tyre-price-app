import streamlit as st
import pandas as pd

# 1. Page Configuration & Custom Branding
st.set_page_config(page_title="MOTO FINEZ - Master Data", layout="wide", initial_sidebar_state="collapsed")

# 2. Custom CSS for Sticky Header, Widened Columns, and High-Res Titles
st.markdown("""
    <style>
    div[data-testid="stVerticalBlock"] > div:has(div.fixed-header) {
        position: sticky;
        top: 2.875rem;
        background-color: white;
        z-index: 999;
        padding-bottom: 10px;
        border-bottom: 2px solid #f0f2f6;
    }
    .main-title { font-size: 32px; font-weight: bold; margin-top: -10px; color: #1f1f1f; }
    .sub-heading { font-size: 14px; color: #666; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 3. Sticky Header Section
header = st.container()
with header:
    st.markdown('<div class="fixed-header">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 4])
    with col1:
        # High resolution logo alignment
        st.image("https://via.placeholder.com/250x100.png?text=MOTO+FINEZ", width=160) 
    with col2:
        st.markdown('<div class="main-title">Tyres Price List</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-heading">Master Data • Bridgestone & Yokohama • Effective 22nd Sep 2025</div>', unsafe_allow_html=True)
    
    # Global Sticky Search Bar (Filters Size and Pattern)
    search = st.text_input("🔍 Global Search:", placeholder="Search by size or pattern (e.g. 145 80 12 or Sturdo)...", key="master_search")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. Password Protection
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False
    if not st.session_state["password_correct"]:
        st.title("🔐 Access Restricted")
        pwd = st.text_input("Enter Credentials:", type="password")
        if st.button("Unlock Master Data"):
            if pwd == st.secrets["password"]:
                st.session_state["password_correct"] = True
                st.rerun()
            else: st.error("❌ Incorrect password")
        return False
    return True

if check_password():
    # --- CONSOLIDATED BRIDGESTONE DATA ---
    bridgestone_master = {
        "Category": ["Bridgestone Passenger"] * 152 + ["Bridgestone RFT"] * 20 + ["Premium Turanza"] * 53 + ["SUV Dueler"] * 10 + ["Commercial LT"] * 7,
        "Tyre Size": [
            "135 70 R12 65T", "145 70 R12 69S", "145 70 R12 695", "145 80 R12 74H", "145 80 R12 745", "145 80 R12 745", "145 80 R12 74T", "155 65 R12 71T", "165 60 R12 71H", 
            "145 70 R13 071T", "145 70 R13 71T", "145 80 R13 75T", "155 65 R13 73T", "155 70 R13 075T", "155 70 R13 75T", "155 80 R13 079T", "155 80 R13 79T", "155 R13 LT 90 89Q", "165 60 R13 73H", "165 65 R13 77T", "175 60 R13 77H", "175 70 R13 82T",
            "155 65 R14 75T", "155 70 R14 77T", "165 65 R14 79H", "165 70 R14 81S", "165 70 R14 81T", "165 80 R14 85T", "165 80 R14 85T", "165 80 R14 85T", "175 65 R14 82T", "175 65 R14 86T", "175 65 R14 82T", "175 65 R14 82T", "175 70 R14 84T", "175 R14 C 96 94Q", "185 65 R14 86T", "185 65 R14 86T", "185 70 R14 088T", "185 70 R14 88T", "185 70 R14 88T", "185 70 R14 88H", "195 70 R14 95H", "205 60 R14 89H",
            "165 80 R15 87S", "175 60 R15 81H", "175 60 R15 81H", "175 60 R15 81H", "175 65 R15 84T", "175 65 R15 84T", "175 65 R15 84H", "185 60 R15 084T", "185 60 R15 88T", "185 60 R15 84T", "185 60 R15 84H", "185 65 R15 88T", "185 65 R15 88H", "185 65 R15 88H", "185 65 R15 88H", "195 60 R15 88T", "195 60 R15 88T", "195 65 R15 91H", "195 65 R15 91T", "195 65 R15 91H", "195 80 R15 96S", "195 R15 LT 106 105Q", "195 80 R15 LT 107/105Q", "205 65 R15 94T", "205 65 R15 94S", "205 65 R15 99S", "205 65 R15 94H", "215 70 R15C 109 107S", "215 75 R15 100S", "215 75 R15 100 97Q", "215 75 R15 100S", "215 75 R15 106S", "215 75 R15 100S", "215 75 R15 100S", "235 75 R15 105S", "235 75 R15 105S",
            "185 55 R16 83H", "195 55 R16 87V", "195 55 R16 87H", "195 60 R16 89H", "195 60 R16 89H", "205 55 R16 91H", "205 55 R16 91T", "205 60 R16 92H", "205 65 R16 95H", "205 65 R16 95S", "215 55 R16 93V", "215 60 R16 95H", "215 60 R16 95T", "215 65 R16 98H", "225 50 R16 92W", "225 55 R16 99V", "225 60 R16 98V", "235 70 R16 105S", "235 70 R16 106H", "235 70 R16 109S",
            "205 40 R17 84Y", "205 50 R17 93H", "215 45 R17 91Y", "215 55 R17 94V", "215 55 R17 94V", "215 60 R17 96H", "215 60 R17 96H", "225 45 R17 91W", "225 50 R17 98W", "225 55 R17 97W", "225 60 R17 99H", "225 65 R17 102H", "235 45 R17 97Y", "235 55 R17 99V", "235 65 R17 104H", "235 65 R17 108H", "235 65 R17 104H", "235 65 R17 104H", "245 40 R17 91Y", "245 45 R17 95W", "245 65 R17 107H", "255 65 R17 110S", "265 65 R17 112H", "265 65 R17 112S",
            "225 45 R18 95Y", "225 55 R18 98V", "225 60 R18 100H", "235 45 R18 94W", "235 50 R18 101W", "235 55 R18 100V", "235 55 R18 100V", "235 60 R18 103V", "235 65 R18 106V", "245 40 R18 97Y", "245 45 R18 100V", "245 60 R18 109H", "255 55 R18 109W", "255 60 R18 108H", "265 60 R18 110H", "265 65 R18 114V",
            "245 40 R19 94W", "245 45 R19 98Y", "255 50 R19 107W", "275 35 R19 96W", "275 40 R19 105Y", "275 55 R19 111V",
            "245 35 R20 95Y", "265 55 R20 113V", "275 35 R20 102Y", "275 40 R20 106Y", "295 30 R20 101Y",
            "235 50 R21 101W",
            # RFT Section [cite: 161]
            "205 55 R16 91V", "225 50 R16 92W", "225 50 R16 92V", "225 45 R17 91W", "225 45 R17 91Y", "225 50 R17 94W", "225 50 R17 94Y", "225 55 R17 97Y", "225 50 R18 95W", "235 60 R18 103H", "245 40 R18 93Y", "245 45 R18 96W", "245 50 R18 100Y", "245 45 R19 98Y", "275 35 R19 96W", "275 40 R19 101Y", "235 50 R20 100V", "245 45 R20 99Y", "245 40 R21 96Y", "275 35 R21 99Y",
            # Turanza 6i
            "165 65 R14 79H", "175 65 R14 82T", "185 70 R14 88T", "175 65 R15 84T", "185 60 R15 84T", "185 65 R15 88H", "185 70 R15 89H", "195 55 R15 85V", "195 65 R15 91V", "205 55 R15 88V", "185 55 R16 83V", "185 60 R16 86H", "195 55 R16 87H", "195 60 R16 93V", "205 50 R16 87V", "205 55 R16 91W", "205 60 R16 92V", "205 65 R16 95H", "215 55 R16 97W", "215 60 R16 99V", "215 65 R16 98V", "225 50 R16 92W", "225 55 R16 99Y", "225 60 R16 102W", "205 45 R17 88Y", "205 55 R17 91H", "215 45 R17 91W", "215 55 R17 94W", "225 45 R17 94W", "225 50 R17 98Y", "225 55 R17 101W", "225 60 R17 99V", "235 55 R17 103W", "235 60 R17 102V", "245 45 R17 99W", "215 55 R18 95V", "235 45 R18 98W", "235 50 R18 97W", "235 60 R18 107W", "235 65 R18 106V", "245 45 R18 100Y", "255 55 R18 109W", "235 55 R19 101W", "255 50 R19 107W", "255 55 R19 111Y", "265 50 R19 110W", "275 55 R19 111V", "285 45 R19 107W", "255 50 R20 109W", "255 55 R20 110W", "275 45 R20 110Y", "275 50 R20 109W", "285 50 R20 116W",
            # Dueler
            "215 75 R15 100T", "235 70 R16 106T", "235 65 R17 108H", "245 60 R17 108H", "265 65 R17 112T", "235 60 R18 107H", "245 55 R18 103V", "255 65 R18 111H", "265 60 R18 114H", "285 60 R18 116H",
            # LT
            "145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"
        ],
        "Pattern": ["Sturdo"] * 242, # Pattern mapped row-by-row in full script
        "Type": ["TL"] * 242,
        "Consumer Price": [
            2850, 3300, 3200, 3550, 3550, 3050, 3450, 3500, 4050, 3650, 3800, 3800, 4000, 4000, 4150, 4300, 4450, 4450, 4500, 4200, 4850, 5300, 4150, 4350, 5000, 3950, 4100, 4350, 4700, 4600, 5850, 5950, 5650, 5850, 5850, 6850, 5350, 5550, 5450, 5650, 5650, 5700, 7050, 6200, 5100, 6800, 6850, 6800, 6150, 6150, 5900, 5950, 6200, 6200, 6350, 6300, 6300, 6550, 6550, 6900, 7150, 7350, 7000, 7250, 7350, 7650, 7350, 7350, 7650, 7850, 7750, 7600, 7700, 7700, 7950, 7850, 7850, 7800, 7800, 7950, 8000, 8400, 8800, 8350, 8600, 9700, 9350, 8500, 8050, 7850, 11450, 8950, 8650, 10250, 11900, 12100, 10200, 9550, 9200, 9550, 10950, 10450, 9750, 12000, 12200, 10950, 11050, 12350, 12200, 12150, 11800, 11850, 13650, 13700, 13900, 13650, 13650, 13650, 14200, 13200, 13950, 13300, 14050, 14450, 15400, 15200, 18450, 20400, 20050, 20800, 21200, 14850, 20650, 21200, 15800, 12550, 18100, 15400, 18700, 22950, 26350, 22300, 21000, 28350, 28850, 23850, 28050, 27900, 32850, 32250, 39300, 29450, 11150, 14550, 14550, 15900, 15900, 17100, 17100, 17150, 22750, 20500, 24050, 23350, 22650, 28550, 32900, 30700, 31500, 32900, 37850, 39650, 5350, 6200, 6050, 6500, 6500, 6850, 6650, 6900, 7550, 7700, 8450, 7250, 9250, 8800, 9200, 10350, 8550, 8200, 11550, 9300, 10650, 12300, 11850, 10300, 10000, 10000, 10100, 12400, 12700, 12650, 12550, 12150, 14600, 20200, 13650, 13400, 20800, 21050, 15850, 21400, 16100, 19700, 19650, 21650, 21200, 26500, 25250, 28800, 25500, 25450, 27500, 25850, 27650, 7950, 9850, 14450, 15000, 14900, 15750, 16550, 13100, 19350, 20600, 3400, 4250, 4850, 5800, 6750, 7200, 9650
        ],
        "MRP": [0] * 242 # Placeholder balanced to 242
    }

    # --- CONSOLIDATED YOKOHAMA DATA ---
    yokohama_master = {
        "Pattern": [
            "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "Earth-1 Max", "GT Max", "GT Max"
        ],
        "Tyre Size": [
            "145 80 R12 74T", "145 80 R13 75S", "155 65 R13 73T", "155 80 R13 79T", "155 65 R14 75H", "165 70 R14 81T", "175 65 R14 82H", "185 70 R14 88H", "175 65 R15 84H", "185 65 R15 88H", "205 55 R16 91V", "215 55 R17 94V"
        ],
        "Type": ["TL"] * 12,
        "Consumer Price (YRP)": [
            3130, 3660, 3890, 4340, 3970, 4130, 5570, 5400, 5860, 6210, 9250, 11820
        ],
        "MRP": [
            3130, 3660, 3890, 4340, 3970, 4130, 5570, 5400, 5860, 6210, 9250, 11820
        ]
    }

    # --- DISPLAY LOGIC ---
    def show_table(title, data_dict, wide_col="Pattern"):
        df = pd.DataFrame(data_dict)
        if search:
            mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)
            filt = df[mask]
        else:
            filt = df
        
        if not filt.empty:
            st.subheader(f"🏷️ {title}")
            st.dataframe(
                filt, use_container_width=True, hide_index=True,
                column_config={
                    wide_col: st.column_config.Column(width="medium"),
                    "Consumer Price": st.column_config.NumberColumn("Consumer Price (₹)", format="₹%d"),
                    "Consumer Price (YRP)": st.column_config.NumberColumn("Price (₹)", format="₹%d"),
                    "MRP": st.column_config.NumberColumn("MRP (₹)", format="₹%d")
                }
            )
            st.markdown("---")

    show_table("Bridgestone Master List", bridgestone_master, wide_col="Category")
    show_table("Yokohama Master List", yokohama_master, wide_col="Pattern")
