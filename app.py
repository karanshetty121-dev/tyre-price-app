import streamlit as st
import pandas as pd

# 1. Function to check password
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state["password_correct"] = False

    if not st.session_state["password_correct"]:
        st.title("🔐 Locked Dashboard")
        pwd = st.text_input("Enter Password to Access Prices:", type="password")
        if st.button("Unlock"):
            # This looks for a secret named 'password' in Streamlit settings
            if pwd == st.secrets["password"]:
                st.session_state["password_correct"] = True
                st.rerun()
            else:
                st.error("❌ Incorrect password")
        return False
    return True

# 2. Only show the app if password is correct
if check_password():
    st.set_page_config(page_title="Tyre Price Finder", layout="centered")

    # Your Data
    data = {
        "Rim": ["12", "13", "14", "14", "15", "15", "15"],
        "Size": ["145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"],
        "Pattern": ["Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400 Plus"],
        "Type": ["TL", "TL", "TL", "TL", "TL", "TL", "TT"],
        "Price": [3400, 4250, 4850, 5800, 6750, 7200, 9650],
        "MRP": [3641, 4574, 5123, 6260, 7283, 7746, 10412]
    }
    df = pd.DataFrame(data)

    st.title("🛞 Bridgestone Price List")
    search = st.text_input("🔍 Search Size or Rim:", placeholder="e.g. 15")

    filt = df[df['Size'].str.contains(search, case=False) | df['Rim'].str.contains(search)] if search else df

    for index, row in filt.iterrows():
        with st.container():
            col1, col2 = st.columns([2, 1])
            with col1:
                st.markdown(f"**{row['Size']}** ({row['Pattern']})")
                st.info(f"Type: {row['Type']}")
            with col2:
                st.markdown(f"### ₹{row['Price']}")
                st.caption(f"MRP: ₹{row['MRP']}")
            st.divider()

