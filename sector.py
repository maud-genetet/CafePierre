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
tab = ['Transport','Industry','Residential','Other','CommercialAndPublicServices','Agriculture']
t = '*100/(Transport+Agriculture+Other+Industry+Residential) AS '
text = ''
for i in tab:
    text += i + t + i +','
text = text[:-1]
df = pd.read_sql_query('SELECT Year, '+text+' FROM Sector', conn)

app = JupyterDash(__name__)

app.layout = html.Div([
    html.H2('Dash Application'),
    html.H1('Pourcentage'),
    dcc.Dropdown(id='Sector_dropdown',
                 value=tab[0], 
                 options=[{'label': Sector, 'value': Sector}
                          for Sector in list(tab)]),
    dcc.Graph(id='PopEvolution')
])

@app.callback(Output('PopEvolution', 'figure'),
              Input('Sector_dropdown', 'value'))
def plot_teams_total(Sector):
    fig = px.bar(df, x='Year', y=Sector, title='Pourcentage')
    return fig

if __name__ == '__main__':
    app.run_server(mode="inline", debug=True)
    pass