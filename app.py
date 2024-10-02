from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/psotogomez/demo1/refs/heads/main/independencia_geocoded_filtered.csv')  

app = Dash()
server=app.server

app.layout = [
    html.H1(children='Independencia Chile', style={'textAlign':'center'}),
    dcc.Dropdown(['MIGRANTE', 'SEXO', 'MAYOR'], 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    return px.scatter(df, x='lat', y='lon',hover_data=['SEXO', 'new_dir', 'RUN'], color=value)

if __name__ == '__main__':
    app.run(debug=True)
