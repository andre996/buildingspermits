import dash 
from dash import html, dcc, dash_table, callback, Input, Output
import dash_design_kit as ddk
import requests
import pandas as pd
import json

dash.register_page(__name__)

# Import and convert data
r = requests.get('https://data.calgary.ca/resource/8ced-xbvn.json')
df = pd.read_json(json.dumps(r.json()))

layout = ddk.Card(
    children=[
    ddk.CardHeader(title='Building raw data'),
    
    ddk.ControlCard(
        orientation='horizontal',
        children=[
            ddk.ControlItem(
                dcc.Dropdown(
                    id='data_selected',
                    multi=True,
                    options=[{"label": i, "value": i} for i in df.columns[0:15]],
                    value=[df.columns[0]]
                ),
                label='Columns selected'
            ),
        ]
    ),

    #adding tables (tables in dash just accept strings, boolean and numbers)
    ddk.DataTable(
        data=df.iloc[:,0:1].to_dict('records'), 
        columns=[{"name": i, "id": i} for i in df.columns[:1]] , 
        id='tbl',
        fixed_rows={'headers': True},
        style_table={'height': '100vh'},
        style_cell={
        'minWidth': 95, 'maxWidth': 95, 'width': 95,    
        })

    ])

@callback(
    Output('tbl', 'data'),
    Output('tbl', 'columns'),
    Input('data_selected', 'value'),
)
def filter_table(prop_selected):
    data=df[prop_selected].to_dict('records')
    columns=[{"name": i, "id": i} for i in prop_selected]
    return data, columns
