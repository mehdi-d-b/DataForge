import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html, no_update, ctx
import diskcache
import requests

from dash_extensions.enrich import (
    #DashProxy,
    #Dash,
    Output,
    Input,
    State,
    dcc,
    html,
    #ServersideOutput,
    #ServersideOutputTransform,
    #OperatorTransform,
    #Operator,
    #OperatorOutput
)
import plotly.graph_objs as go

import pages.data_table as data_table
import pages.status as status


cache = diskcache.Cache("./cache")
background_callback_manager = dash.DiskcacheManager(cache)


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
    suppress_callback_exceptions=True,
    update_title=None,
    prevent_initial_callbacks=True,
    background_callback_manager=background_callback_manager
)



# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("DataForge", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Description ici.",
                    className="lead",
                )
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Status", href="/", active="exact"),
                    dbc.NavLink("Data List", href="/data-list", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="page-content")

app.layout = html.Div([
    dcc.Location(id="url"), 
    sidebar, 
    content,
    dcc.Store(id='store-tags', storage_type='local')
    ])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return status.layout
    elif pathname == "/data-list":
        return data_table.layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""

@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("plc-grid", "rowTransaction"),
    Input("btn-rmv-plc", "n_clicks"),
    Input("btn-add-plc", "n_clicks"),
    State("plc-grid", "selectedRows"),
)
def update_plc_rowdata(n1, n2, selection):

    if ctx.triggered_id == "btn-rmv-plc":
        if selection is None:
            return no_update
        return {"remove": selection}

    if ctx.triggered_id == "btn-add-plc":
        newRows = []
        return {"add": newRows}
    

@app.callback(
    Output("tag-grid", "rowTransaction"),
    Input("btn-load-tag", "n_clicks"),
)
def update_tag_rowdata(n1):

    if ctx.triggered_id == "btn-load-tag":
        newRows = []
        kafka_connect_url = "http://<votre_adresse_kafka_connect>:8083"
        connector_name = "<nom_du_connecteur_plc4x>"        
        url = f"{kafka_connect_url}/connectors/{connector_name}/config"
        response = requests.get(url)
        print(response)
        return {"add": newRows}


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)