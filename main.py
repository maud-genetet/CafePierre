from re import X
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px
import sqlite3 as sql

conn = sql.connect('./bd/DB.db')

# ['countryCode', 'Year', 'GDP', 'Population', 'CarbonFootprint', 'GHG']
df = pd.read_sql_query("SELECT countryCode, population, Year FROM CountryInformations", conn)


app = JupyterDash(__name__)

app.layout = html.Div([
    html.H2('Dash Application'),
    html.H1('Population Evolution (1992 - 2020)'),
    dcc.Dropdown(id='Country_dropdown',
                 value=df['countryCode'].values[0], 
                 options=[{'label': year, 'value': year}
                          for year in list(df['countryCode'].unique())]),
    dcc.Graph(id='PopEvolution'),
])

@app.callback(Output('PopEvolution', 'figure'),
              Input('Country_dropdown', 'value'))
def plot_teams_total(year):
    df_year = df[df['countryCode'] == year]
    fig = px.line(
        df_year,
        x='Year',
        y='Population',
        height=200 + 50 * len(df['countryCode'].unique()),
        title= f'Population - {year} ',
    )
    return fig

if __name__ == '__main__':
    app.run_server(mode="inline", debug=True)
    pass