import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_excel(
    io=r'G:\Dash Working\assignment 1.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1',
    usecols='A:E',
    nrows=77
)
print(df)
app = dash.Dash()

#html Layout for Dashboard

app.layout = html.Div(children=[
    html.H1(children='Analysis Dashboard'),
    dcc.Dropdown(id='borrower-dropdown',
    options=[{'label':i, 'value':i}
        for i in df ['Borrower'].unique()],
    value='')
    dcc.Graph(id='borrower-Graph')])

