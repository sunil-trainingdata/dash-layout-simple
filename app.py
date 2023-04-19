# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(className='row', children=[
    dbc.Row([
        dbc.Col(
            html.H1(children='Hello Dash Updated',id='f7f9f0e1-05b1-4547-8590-ffbbe271c4d8'),
            width={"size": 12},
        ), 
        dbc.Col(
            dcc.Graph(id='example-graph', figure={'data': [{"alignmentgroup":"True","hovertemplate":"City=SF<br>Fruit=%{x}<br>Amount=%{y}<extra></extra>","legendgroup":"SF","marker":{"color":"#636efa","pattern":{"shape":""}},"name":"Dataset #1","offsetgroup":"SF","orientation":"v","showlegend":true,"textposition":"auto","type":"bar","x":["Apples","Oranges","Bananas"],"xaxis":"x","y":[4,1,2],"yaxis":"y"},{"alignmentgroup":"True","hovertemplate":"City=Montreal<br>Fruit=%{x}<br>Amount=%{y}<extra></extra>","legendgroup":"Montreal","marker":{"color":"#EF553B","pattern":{"shape":""}},"name":"Dataset #2","offsetgroup":"Montreal","orientation":"v","showlegend":true,"textposition":"auto","type":"bar","x":["Apples","Oranges","Bananas"],"xaxis":"x","y":[2,4,5],"yaxis":"y"}]}),
            width={"size": 12},
        ),
    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)
