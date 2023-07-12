import dash
from dash import html, dcc;
import dash_design_kit as ddk


dash.register_page(__name__, image='assets\share.jpg')

layout =  ddk.Card(
            children=[
               ddk.CardHeader(title='Building inspection map')
            ]
)