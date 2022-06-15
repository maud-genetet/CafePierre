from re import X
from unittest import case
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import sqlite3 as sql

conn = sql.connect('./bd/DB.db')

# ['countryCode', 'Year', 'GDP', 'Population', 'CarbonFootprint', 'GHG']
# df = pd.read_sql_query("SELECT SUM(Biomass_and_Waste) AS Biomass_and_Waste, SUM(Coal) AS Coal, SUM(Crude_Oil) AS Crude_Oil, SUM(Electricity) AS Electricity, SUM(Gas) AS Gas, SUM(Geothermal) AS Geothermal, SUM(Heat) AS Heat, SUM(OilProducts) AS OilProducts FROM Energy", conn)
df = pd.read_sql_query("SELECT Year, SUM(Biomass_and_Waste + Coal + Crude_Oil + Electricity + Gas + Geothermal + Heat + OilProducts) AS Total FROM Energy GROUP BY Year", conn) 

app = JupyterDash(__name__)
fig = px.bar(df, x='Year', y='Total', title='Total Energy Consumption')
app.layout = html.Div([
    html.H2('Dash Application'),
    dcc.Graph(figure = fig)
    #dcc.Graph(id='PopEvolution')
])



if __name__ == '__main__':
    app.run_server(debug=True)
    pass