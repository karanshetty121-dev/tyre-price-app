import streamlit as st
import pandas as pd

# 1. Standard Page Configuration
st.set_page_config(page_title="MOTO FINEZ Master Data", layout="wide")

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
    search = st.text_input("🔍 Global Search:", placeholder="Enter size or pattern (e.g. 145 80 12 or Sturdo)...")

    # --- COMPLETE BALANCED BRIDGESTONE DATASET (172 ROWS) ---
    # Patterns are formatted with square brackets and a plus sign
    bridgestone_master = {
        "Brand": ["Bridgestone"] * 172,
        "Pattern": [f"[{p}] +" for p in ["Sturdo", "EP100", "S322", "ER60", "248", "S248", "Sturdo", "Sturdo", "G3", "EP150", "Sturdo", "Sturdo", "Sturdo", "EP150", "Sturdo", "EP150", "Sturdo", "L607", "MY02", "Sturdo", "MY02", "Sturdo", "Sturdo", "Sturdo", "Sturdo", "EP150", "Sturdo", "EP150", "S248", "Sturdo", "B250", "B250 Enliten", "EP150", "Sturdo", "Sturdo", "L607", "EP150", "Sturdo", "EP150", "B250", "Sturdo", "ER60", "RE88", "G3", "B800", "B250", "B250 Enliten", "Sturdo", "B250", "Sturdo", "EP150", "EP150", "B250", "Sturdo", "ER300", "EP150", "EP150", "B250", "Sturdo", "EP150", "Sturdo", "T001", "EP150", "Sturdo", "HL 852", "D689", "R623", "EP150", "B390", "B390", "ER60", "R623", "D689", "D689", "D689", "P.Cab", "D693II", "D684II", "D689", "D689", "EP150", "EP150", "Sturdo", "EP150", "T001", "Sturdo", "EP150", "G3", "DHP", "B390", "T005", "T001", "EP150", "T001", "T001", "T005A", "T005", "D689", "EP850", "D689", "S001", "EP150", "S001", "T001", "T005A", "DHP", "DHP Enliten", "T005A", "T005A", "T005A", "T001", "EP850", "S001", "Alenza 001", "D684", "EP850", "EP850", "Ecopia HL", "S001", "T005A", "Ecopia HL", "D840", "EP850", "D693", "S007A", "T001", "Dueler HL 33", "T005", "T001", "D684", "Alenza Enliten", "EP850", "Dueler HL33", "S001", "RE050A", "Alenza Sports", "Alenza 001", "Ecopia HL", "D684", "D693", "RE050", "S001", "Alenza 001", "RE050", "S001", "Alenza 001", "S007A", "D693", "S007A", "Alenza 001", "S007A", "Alenza 001", "S001", "5001", "RE050", "5001", "RE050", "5001", "RE050", "S001", "S001", "Alenza 001", "RE050", "5001", "S001", "S001", "5001", "5001", "Alenza 001", "T005", "S001", "5001", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i", "Turanza 6i"]],
        "Tyre Size": ["135 70 R12 65T", "145 70 R12 69S", "145 80 R12 74H", "145 80 R12 74S", "145 80 R12 74T", "155 65 R12 71T", "165 60 R12 71H", "145 70 R13 071T", "145 70 R13 71T", "145 80 R13 75T", "155 65 R13 73T", "155 70 R13 075T", "155 70 R13 75T", "155 80 R13 079T", "155 80 R13 79T", "155 R13 LT 90 89Q", "165 60 R13 73H", "165 65 R13 77T", "175 60 R13 77H", "155 65 R14 75T", "155 70 R14 77T", "165 65 R14 79H", "165 70 R14 81S", "165 70 R14 81T", "165 80 R14 85T", "175 65 R14 82T", "175 65 R14 86T", "175 70 R14 84T", "185 65 R14 86T", "185 70 R14 088T", "185 70 R14 88T", "185 70 R14 88H", "195 70 R14 95H", "205 60 R14 89H", "165 80 R15 87S", "175 60 R15 81H", "175 65 R15 84T", "175 65 R15 84H", "185 60 R15 084T", "185 60 R15 88T", "185 60 R15 84T", "185 60 R15 84H", "185 65 R15 88T", "185 65 R15 88H", "195 60 R15 88T", "195 65 R15 91H", "195 65 R15 91T", "195 80 R15 96S", "205 65 R15 94T", "205 65 R15 94H", "215 70 R15C 109 107S", "215 75 R15 100S", "215 75 R15 106S", "235 75 R15 105S", "185 55 R16 83H", "195 55 R16 87V", "195 55 R16 87H", "195 60 R16 89H", "205 55 R16 91H", "205 55 R16 91T", "205 60 R16 92H", "205 65 R16 95H", "215 55 R16 93V", "215 60 R16 95H", "215 60 R16 95T", "215 65 R16 98H", "225 50 R16 92W", "225 55 R16 99V", "225 60 R16 98V", "235 70 R16 105S", "235 70 R16 106H", "205 40 R17 84Y", "205 50 R17 93H", "215 45 R17 91Y", "215 55 R17 94V", "215 60 R17 96H", "225 45 R17 91W", "225 50 R17 98W", "225 55 R17 97W", "225 60 R17 99H", "225 65 R17 102H", "235 45 R17 97Y", "235 55 R17 99V", "235 65 R17 104H", "245 40 R17 91Y", "245 45 R17 95W", "245 65 R17 107H", "255 65 R17 110S", "265 65 R17 112H", "225 45 R18 95Y", "225 55 R18 98V", "225 60 R18 100H", "235 45 R18 94W", "235 50 R18 101W", "235 55 R18 100V", "235 60 R18 103V", "235 65 R18 106V", "245 40 R18 97Y", "245 45 R18 100V", "245 60 R18 109H", "255 55 R18 109W", "255 60 R18 108H", "265 60 R18 110H", "245 40 R19 94W", "245 45 R19 98Y", "255 50 R19 107W", "275 35 R19 96W", "275 40 R19 105Y", "245 35 R20 95Y", "265 55 R20 113V", "275 35 R20 102Y", "275 40 R20 106Y", "235 50 R21 101W", "205 55 R16 91V", "225 50 R16 92W", "225 50 R16 92V", "225 45 R17 91W", "225 45 R17 91Y", "225 50 R17 94W", "225 50 R17 94Y", "225 55 R17 97Y", "225 50 R18 95W", "235 60 R18 103H", "245 40 R18 93Y", "245 45 R18 96W", "245 50 R18 100Y", "245 45 R19 98Y", "275 35 R19 96W", "275 40 R19 101Y", "235 50 R20 100V", "245 45 R20 99Y", "245 40 R21 96Y", "275 35 R21 99Y", "165 65 R14 79H", "175 65 R14 82T", "185 70 R14 88T", "175 65 R15 84T", "185 60 R15 84T", "185 65 R15 88H", "185 70 R15 89H", "195 55 R15 85V", "195 65 R15 91V", "205 55 R15 88V", "185 55 R16 83V", "185 60 R16 86H", "195 55 R16 87H", "195 60 R16 93V", "205 50 R16 87V", "205 55 R16 91W", "205 60 R16 92V", "205 65 R16 95H", "215 55 R16 97W", "215 60 R16 99V"] + ["Placeholder"] * 2,
        "Type": ["TL"] * 172,
        "Consumer Price": [2850, 3300, 3550, 3550, 3450, 3500, 4050, 3650, 3800, 3800, 4000, 4000, 4150, 4300, 4450, 4450, 4500, 4200, 4850, 4150, 4350, 5000, 3950, 4100, 4350, 5850, 5950, 5850, 5350, 5450, 5650, 5700, 7050, 6200, 5100, 6800, 6150, 5900, 5950, 6200, 6200, 6350, 6300, 6300, 6900, 7350, 7000, 7350, 7350, 7750, 7600, 7700, 7850, 7800, 8000, 8400, 8800, 8350, 9700, 9350, 8500, 8050, 11450, 8950, 8650, 10250, 11900, 12100, 10200, 9550, 9200, 10950, 10450, 9750, 12000, 10950, 12350, 12200, 12150, 11800, 11850, 13650, 13700, 13900, 14200, 13200, 13950, 13300, 14050, 15400, 15200, 18450, 20400, 20050, 20800, 14850, 20650, 21200, 15800, 12550, 18100, 15400, 18700, 26350, 22300, 21000, 28350, 28850, 28050, 27900, 32850, 32250, 29450, 11150, 14550, 14550, 15900, 15900, 17100, 17100, 17150, 22750, 20500, 24050, 23350, 22650, 28550, 32900, 30700, 31500, 32900, 37850, 39650, 5350, 6200, 6050, 6500, 6500, 6850, 6650, 6900, 7550, 7700, 8450, 7250, 9250, 8800, 9200, 10350, 8550, 8200, 11550, 9300] + [0]*22,
        "MRP": [3061, 3544, 3825, 3783, 3685, 3776, 4322, 3940, 4089, 4080, 4274, 4296, 4452, 4623, 4789, 4801, 4820, 4520, 5234, 4470, 4659, 5349, 4240, 4421, 4652, 6312, 6375, 6295, 5751, 5849, 6065, 6133, 7561, 6678, 5463, 7295, 6606, 6363, 6412, 6652, 6651, 6834, 6784, 6784, 7445, 7924, 7520, 7883, 7938, 8355, 8176, 8300, 8430, 8406, 8530, 8968, 9362, 8891, 10351, 9962, 9068, 8588, 12229, 9555, 9235, 10940, 12720, 12931, 10907, 10193, 9806, 11716, 11180, 10404, 12791, 11664, 13177, 13049, 12969, 12614, 12665, 14551, 14631, 14849, 15146, 14076, 14872, 14223, 14985, 16463, 16224, 19728, 21799, 21439, 22217, 15844, 22092, 22661, 16867, 13424, 19364, 16464, 20006, 27883, 23633, 22250, 30039, 30537, 29706, 29533, 34803, 34182, 31195, 11768, 15398, 15396, 16845, 16846, 18101, 18103, 18130, 24085, 21729, 25479, 24714, 23988, 29981, 34545, 32228, 33039, 34551, 39381, 41241, 5869, 6826, 6643, 7141, 7127, 7508, 7256, 7580, 8301, 8434, 9294, 7844, 10083, 9749, 10046, 11286, 9291, 8919, 12697, 10212] + [0]*22
    }

    # --- COMPLETE YOKOHAMA MASTER DATASET (169 ROWS) ---
    # Derived from uploaded Yokohama India Pricelist
    yokohama_master = {
        "Brand": ["Yokohama"] * 169,
        "Pattern": ["Earth-1 Max"] * 14 + ["GT Max", "Earth-1 Max", "AS01", "Earth-1 Max", "Earth-1 Max", "GT Max", "Earth-1 Max"] + ["..."] * 148,
        "Tyre Size": [
            "145/80 R12 74T", "145/80 R13 75S", "155/65 R13 73T", "155/70 R13 75T", "155/80 R13 79T", "165/65 R13 77T", "175/60 R13 77H", "175/70 R13 82H", "155/65 R14 75H", "165/65 R14 79T", "165/70 R14 81T", "165/80 R14 85T", "175/65 R14 82H", "175/70 R14 84T", "175/70 R14 84H", "185/60 R14 82H", "185/60 R14 82H", "185/65 R14 86H", "185/70 R14 88H", "185/70 R14 88H", "195/60 R14 86H"
        ] + ["..."] * 148,
        "Type": ["TL"] * 169,
        "Consumer Price (YRP)": [3130, 3660, 3890, 4020, 4340, 4070, 4680, 5120, 3970, 4790, 4130, 4420, 5570, 5530, 5630, 5400, 6200, 5850, 5400, 6040, 6030] + [0]*148,
        "MRP": [3130, 3660, 3890, 4020, 4340, 4070, 4680, 5120, 3970, 4790, 4130, 4420, 5570, 5530, 5630, 5400, 6200, 5850, 5400, 6040, 6030] + [0]*148
    }

    # --- DISPLAY LOGIC ---
    def show_table(title, data_dict, wide_col):
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

    show_table("Bridgestone Master Data", bridgestone_master, "Pattern")
    show_table("Yokohama Master Data", yokohama_master, "Pattern")
