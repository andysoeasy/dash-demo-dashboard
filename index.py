from frontend.layouts import page_content
from backend.app import app
from dash import html, dcc

import backend.callbacks

from frontend.navbar import navbar

location = dcc.Location(id = 'url', refresh = False)

app.layout = html.Div([
    navbar,
    location,
    page_content
])
app.run(debug = True, 
        # host = '192.168.100.7', 
        port = '8050')