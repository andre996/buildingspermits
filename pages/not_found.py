from dash import html
import dash


dash.register_page(__name__)

layout = html.Div([html.Img(src="assets/not-found-404.jpg")])