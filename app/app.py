import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc
import numpy as np
import plotly.express as px

app = dash.Dash(__name__)

docker = True
server = app.server


@app.callback(
    Output("histogramm", "figure"),
    Input("stichprobe", "value"),
)
def generate_hist(n):
    return px.histogram(np.random.normal(loc=0, scale=1, size=n))


app.layout = html.Div(
    children=[
        html.H1(children="Verteilungen"),
        html.Div(
            children=[
                dcc.Input(
                    id="stichprobe",
                    placeholder="Stichprobe",
                    type="number",
                    value=100,
                ),
            ],
        ),
        html.Div(
            children=[
                html.H2("Histogramm"),
                dcc.Graph(id="histogramm"),
            ],
        ),
    ]
)
#dcc.Graph(id="histogramm", figure=generate_hist(100)),

if __name__ == "__main__":
    if docker:
        app.run_server(debug=True, host="0.0.0.0", port=8080, use_reloader=False)
    else:
        app.run_server(debug=True)

# docker run -p 8080:80
