import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Tyre Price Dashboard", layout="wide")

# Header
st.title("🛞 Bridgestone Price Dashboard")
st.caption("Official Prices - Effective 22nd Sept 2025")

# [span_1](start_span)Data from your PDF[span_1](end_span)
data = {
    "Rim": ["12", "13", "14", "14", "15", "15", "15"],
    "Size": ["145 R12", "155 R13", "165 R14", "185 R14", "195 R15", "215 75 R15", "7.00 R15"],
    "Pattern": ["Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400", "Duravis R400 Plus"],
    "Type": ["TL", "TL", "TL", "TL", "TL", "TL", "TT"],
    "Price (₹)": [3400, 4250, 4850, 5800, 6750, 7200, 9650],
    "MRP (₹)": [3641, 4574, 5123, 6260, 7283, 7746, 10412]
}

df = pd.DataFrame(data)

# High-Speed Search Bar
search_query = st.text_input("⚡ Search by Size or Rim:", placeholder="Type here...")

# Filter logic
if search_query:
    filtered_df = df[
        df['Size'].str.contains(search_query, case=False) | 
        df['Rim'].str.contains(search_query) |
        df['Pattern'].str.contains(search_query, case=False)
    ]
else:
    filtered_df = df

# Displaying the Table
st.dataframe(
    filtered_df, 
    use_container_width=True, 
    hide_index=True,
    column_config={
        "Price (₹)": st.column_config.NumberColumn(format="₹%d"),
        "MRP (₹)": st.column_config.NumberColumn(format="₹%d")
    }
)

st.info("💡 Pro Tip: Tap the top of any column to sort by price or size.")
