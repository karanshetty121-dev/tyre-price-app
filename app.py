import streamlit as st
import pandas as pd

# This must be the first command
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
    st.title("🛞 Bridgestone Price List")
    
    # 1. ADD YOUR DATA HERE
    # Just add more items to these lists. Make sure every list has the SAME number of items.
    data = {
        "Product Code": ["BS-001", "BS-002", "BS-003", "BS-004", "BS-005", "BS-006", "BS-007"],
        "Rim": ["12", "13", "14", "14", "15", "15", "15"],
        "Size": ["145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"],
        "Pattern": ["Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400 Plus"],
        "Type": ["TL", "TL", "TL", "TL", "TL", "TL", "TT"],
        "Price": [3400, 4250, 4850, 5800, 6750, 7200, 9650],
        "MRP": [3641, 4574, 5123, 6260, 7283, 7746, 10412]
    }
    
    df = pd.DataFrame(data)

    # 2. Search & Filter
    search = st.text_input("🔍 Quick Search:", placeholder="Search Size, Pattern, or Code...")
    
    if search:
        # Search across multiple columns at once
        filt = df[
            df['Size'].str.contains(search, case=False) | 
            df['Pattern'].str.contains(search, case=False) |
            df['Product Code'].str.contains(search, case=False) |
            df['Rim'].str.contains(search)
        ]
    else:
        filt = df

    # 3. Display as Interactive Table
    # use_container_width=True makes it fill the phone screen
    st.dataframe(
        filt, 
        use_container_width=True, 
        hide_index=True,
        column_config={
            "Price": st.column_config.NumberColumn("Our Price", format="₹%d"),
            "MRP": st.column_config.NumberColumn("MRP", format="₹%d"),
        }
    )

    if st.sidebar.button("Log Out"):
        st.session_state["password_correct"] = False
        st.rerun()


