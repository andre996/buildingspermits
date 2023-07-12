from dash import Dash, html, dcc, callback, Output, Input, dash_table, page_registry, page_container
import dash_design_kit as ddk
import requests
import pandas as pd
import json


# Import and convert data
r = requests.get('https://data.calgary.ca/resource/8ced-xbvn.json')
df = pd.read_json(json.dumps(r.json()))


app = Dash(__name__, use_pages=True)
server = app.server  # expose server variable for Procfile

theme = {
    "accent":"#fa4f56",
    "accent_positive":"#33ffe6",
    "accent_negative":"#ff2c6d",
    "background_content":"#F2F2F2",
    "background_page":"#F9F9F9",
    "body_text":"#606060",
    "border":"#e2e2e2",
    "border_style":{
        "name":"underlined",
        "borderWidth":"0px 0px 1px 0px",
        "borderStyle":"solid",
        "borderRadius":0
    },
    "button_border":{
        "width":"1px",
        "color":"#fa4f56",
        "radius":"0px"
    },
    "button_capitalization":"capitalize",
    "button_text":"#fa4f56",
    "button_background_color":"#F2F2F2",
    "control_border":{
        "width":"1px",
        "color":"#e2e2e2",
        "radius":"5px"
    },
    "control_background_color":"#F2F2F2",
    "control_text":"#606060",
    "card_margin":"15px",
    "card_padding":"5px",
    "card_border":{
        "width":"1px",
        "style":"solid",
        "color":"#e2e2e2",
        "radius":"0px"
    },
    "card_background_color":"#F2F2F2",
    "card_box_shadow":"1px 1px 1px 0 #e80a0a",
    "card_outline":{
        "width":"0px",
        "style":"solid",
        "color":"#e2e2e2"
    },
    "card_header_margin":"0px",
    "card_header_padding":"10px",
    "card_header_border":{
        "width":"0px 0px 2px 0px",
        "style":"dashed",
        "color":"#e2e2e2",
        "radius":"0px"
    },
    "card_header_background_color":"#F2F2F2",
    "card_header_box_shadow":"0px 0px 0px rgba(0,0,0,0)",
    "breakpoint_font":"1200px",
    "breakpoint_stack_blocks":"700px",
    "colorway":[
        "#fa4f56",
        "#4c78a8",
        "#f58518",
        "#72b7b2",
        "#54a24b",
        "#eeca3b",
        "#b279a2",
        "#ff9da6",
        "#9d755d",
        "#bab0ac"
    ],
    "colorscale":[
        "#fa4f56",
        "#fe6767",
        "#ff7c79",
        "#ff908b",
        "#ffa39d",
        "#ffb6b0",
        "#ffc8c3",
        "#ffdbd7",
        "#ffedeb",
        "#ffffff"
    ],
    "dbc_primary":"#fa4f56",
    "dbc_secondary":"#898989",
    "dbc_info":"#6BB4DD",
    "dbc_gray":"#adb5bd",
    "dbc_success":"#709A00",
    "dbc_warning":"#eeca3b",
    "dbc_danger":"#FF7190",
    "font_family":"Raleway",
    "font_family_header":"Roboto",
    "font_family_headings":"Roboto",
    "font_size":"17px",
    "font_size_smaller_screen":"15px",
    "font_size_header":"24px",
    "title_capitalization":"capitalize",
    "header_content_alignment":"spread",
    "header_margin":"0px 0px 15px 0px",
    "header_padding":"0px",
    "header_border":{
        "width":"0px",
        "style":"none",
        "color":"#e2e2e2",
        "radius":"0px"
    },
    "header_background_color":"#F2F2F2",
    "header_box_shadow":"none",
    "header_text":"#606060",
    "heading_text":"#606060",
    "text":"#606060",
    "report_background_content":"#FAFBFC",
    "report_background_page":"white",
    "report_text":"black",
    "report_font_family":"Computer Modern",
    "report_font_size":"12px"
}

app.layout = ddk.App(show_editor=True, theme=theme,children=[
    ddk.Sidebar(
        foldable=True,
        children=[
            ddk.Logo(src=app.get_asset_url('logo-calgary.png')),
            ddk.Title('Building', capitalization='capitalize'),
            # Inside the menu there is a comprehensive list to auto generate the
            # dcc.link of the menu
            ddk.Menu([
                ddk.Block(
                    dcc.Link(
                        [
                            # Display the icones
                            # Question: can I use ddk.Icon with my own icones? 
                            ddk.Logo(src=app.get_asset_url(f"icon-{page['name']}.png"),
                                    style={'height': '40px', 'width': 'auto'}),
                            # Register removes "_" in the names 
                            f"{page['name']}"
                        ], 
                        href=page["relative_path"]
                    )
                )
                # Iterate through all the pages registered
                for page in page_registry.values()
            ])
        ]
    ),    
    ddk.SidebarCompanion(
        page_container
    )
])
    

    # This code generate the links to the pages
    # html.Div([
    #     html.Div(
    #         dcc.Link(
    #             
    #             f"{page['name']} - {page['path']}", href=page["relative_path"]
    #             )
    #         )
    
    #     for page in page_registry.values()
    # ]),

    # Indicate where the page content should be display, 
    # the content in app.py file will be in all the pages
    #page_container,

    # html.Div([
    #     # adding tables (tables in dash just accept strings, boolean and numbers)
    # dash_table.DataTable(df.iloc[:,0:15].to_dict('records'), [{"name": i, "id": i} for i in df.columns[:15]] , id='tbl')
    # ])
    
    #])


if __name__ == '__main__':
    app.run(debug=True)
