import streamlit as st
import pandas as pd

# -------------------------------------------------
# 1. PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="MOTO FINEZ – Bridgestone Master Data",
    layout="wide"
)

# -------------------------------------------------
# 2. CUSTOM STYLES
# -------------------------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 32px;
    font-weight: bold;
    margin-top: -20px;
}
.sub-heading {
    font-size: 14px;
    color: gray;
    margin-bottom: 20px;
}
.disclaimer {
    font-size: 12px;
    color: #b00;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# 3. HEADER
# -------------------------------------------------
col1, col2 = st.columns([1, 4])
with col1:
    st.image(
        "https://via.placeholder.com/150x150.png?text=MOTO+FINEZ",
        width=120
    )
with col2:
    st.markdown(
        '<div class="main-title">Tyres Price List</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="sub-heading">Master Data – Bridgestone India (Internal Reference)</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="disclaimer">⚠ Prices are indicative. Not for direct customer circulation.</div>',
        unsafe_allow_html=True
    )

# -------------------------------------------------
# 4. PASSWORD PROTECTION
# -------------------------------------------------
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if not st.session_state.password_correct:
        st.title("🔐 Access Required")
        pwd = st.text_input("Enter MOTO FINEZ Credentials", type="password")

        if st.button("Unlock Master Data"):
            if pwd == st.secrets.get("password", ""):
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("❌ Invalid password")

        return False
    return True

if not check_password():
    st.stop()

# Logout
if st.sidebar.button("🚪 Logout"):
    st.session_state.password_correct = False
    st.rerun()

# -------------------------------------------------
# 5. DATA (UNCHANGED – YOUR MASTER DATA)
# -------------------------------------------------
bridgestone_master = {
    "Category": (
        ["Passenger (BSID)"] * 152 +
        ["Run-Flat (RFT)"] * 20 +
        ["Premium (Turanza 6i)"] * 53 +
        ["SUV (Dueler)"] * 10 +
        ["Commercial (LT)"] * 7
    ),
    "Rim": (
        ["12"]*9 + ["13"]*13 + ["14"]*22 + ["15"]*36 + ["16"]*20 +
        ["17"]*24 + ["18"]*16 + ["19"]*6 + ["20"]*5 + ["21"]*1 +
        ["16"]*3 + ["17"]*5 + ["18"]*5 + ["19"]*3 + ["20"]*2 + ["21"]*2 +
        ["14"]*3 + ["15"]*7 + ["16"]*14 + ["17"]*11 + ["18"]*7 + ["19"]*5 + ["20"]*6 +
        ["15","16","17","17","17","18","18","18","18","18"] +
        ["12","13","14","14","15","15","15"]
    ),
    "Tyre Size": [...],   # 🔴 KEEP YOUR FULL TYRE SIZE LIST HERE (UNCHANGED)
    "Pattern": [...],     # 🔴 KEEP YOUR FULL PATTERN LIST HERE (UNCHANGED)
    "Type": ["Tubeless / RFT / Tube"] * 242,
    "Consumer Price": [...],  # 🔴 KEEP FULL LIST
    "MRP": [...]              # 🔴 KEEP FULL LIST
}

# -------------------------------------------------
# 6. DATAFRAME + SAFETY CHECK
# -------------------------------------------------
lengths = {k: len(v) for k, v in bridgestone_master.items()}
if len(set(lengths.values())) != 1:
    st.error("❌ Data error: Column length mismatch")
    st.json(lengths)
    st.stop()

df = pd.DataFrame(bridgestone_master)

# -------------------------------------------------
# 7. SIDEBAR FILTERS
# -------------------------------------------------
st.sidebar.header("🔧 Filters")

category_filter = st.sidebar.multiselect(
    "Category",
    sorted(df["Category"].unique())
)

rim_filter = st.sidebar.multiselect(
    "Rim Size",
    sorted(df["Rim"].unique())
)

pattern_filter = st.sidebar.multiselect(
    "Pattern",
    sorted(df["Pattern"].unique())
)

if category_filter:
    df = df[df["Category"].isin(category_filter)]
if rim_filter:
    df = df[df["Rim"].isin(rim_filter)]
if pattern_filter:
    df = df[df["Pattern"].isin(pattern_filter)]

# -------------------------------------------------
# 8. GLOBAL SEARCH (OPTIMIZED)
# -------------------------------------------------
search = st.text_input(
    "🔍 Global Search",
    placeholder="Search size, pattern, rim, category…"
)

df["_search"] = df.astype(str).agg(" ".join, axis=1)

if search:
    df = df[df["_search"].str.contains(search, case=False)]

df = df.drop(columns="_search")

# -------------------------------------------------
# 9. TABLE DISPLAY
# -------------------------------------------------
st.subheader("📊 Bridgestone India – Master Price Data")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Consumer Price": st.column_config.NumberColumn(
            "Consumer Price (₹)", format="₹{:,.0f}"
        ),
        "MRP": st.column_config.NumberColumn(
            "MRP (₹)", format="₹{:,.0f}"
        )
    }
)

# -------------------------------------------------
# 10. DOWNLOAD
# -------------------------------------------------
st.download_button(
    "⬇️ Download Filtered Price List (CSV)",
    df.to_csv(index=False),
    file_name="bridgestone_master_price_list.csv",
    mime="text/csv"
)
