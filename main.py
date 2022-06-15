from re import X
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('./bd/GreenhouseGasWorld.csv', sep=';')

# Pivot
df = df.iloc[1:,:]
df.columns = ['Year', 'GHG']
df = df[df.Year >= "1992-00-00"]   
df["Year"] = df["Year"].str[0:4]
df["Year"] = df["Year"].astype(int)
df["GHG"] = df["GHG"].str.replace(',', '.')
df["GHG"] = df["GHG"].astype(float)
df.fillna(0, inplace=True)
df.reset_index(drop=False, inplace=True )
print(df.head())

app = JupyterDash(__name__)

app.layout = html.Div([
    html.H2('Dash Application'),
    html.H1('Sea Level Rise'),
    dcc.Dropdown(id='year_dropdown',
                 value=2016,
                 options=[{'label': year, 'value': year}
                          for year in list(df["Year"].unique())]),
    dcc.Graph(id='GreenHouseGas'),
])

@app.callback(Output('GreenHouseGas', 'figure'),
              Input('year_dropdown', 'value'))
def plot_teams_total(year):
    fig = px.line(
        df,
        x='Year',
        y='GHG',
        height=200 + 15*15,
        title= f'Greenhouse Gas - {year} ',
    )
    fig.update_layout(yaxis_categoryorder='total ascending')
    return fig

if __name__ == '__main__':
    app.run_server(mode="inline", debug=True)