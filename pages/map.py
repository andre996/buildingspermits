import dash
from dash import html, dcc;
import dash_design_kit as ddk
import requests
import pandas as pd
import json


# Import and convert data
r = requests.get('https://data.calgary.ca/resource/8ced-xbvn.json')
df = pd.read_json(json.dumps(r.json()))

dash.register_page(__name__, image='assets\share.jpg')

layout =  ddk.Card(
            children=[
               ddk.CardHeader(title='Building Inspection Map')
            ]
)