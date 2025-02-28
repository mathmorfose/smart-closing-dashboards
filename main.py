from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Smart Closing Dashboards",
    layout="wide"
)

st.title("Build your own Smart Closing Dashboard")

# Upload button
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls"])

# Process the file if uploaded
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    pyg_app = StreamlitRenderer(df)
    
    pyg_app.explorer()