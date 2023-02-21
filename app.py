import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Analysis Interactive Dashboard",
                    page_icon=":bar_chart:",
                    layout="wide"

)

df = pd.read_excel(
    io=r'G:\Dash Working\assignment 1.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:E',
    nrows=77
)

st.sidebar.header("Please Filter Here:")
x  = st.sidebar.multiselect("Borrower", options=df['Borrower'].unique(), default=df['Borrower'].unique())

y = st.sidebar.multiselect("Loan_Type", options=df['Loan_Type'].unique(), default=df['Loan_Type'].unique())

df_selection = df.query("Borrower == @x & Loan_Type == @y")

st.dataframe(df_selection)




