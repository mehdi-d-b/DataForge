from dash import Dash, dash_table, html
import pandas as pd
from collections import OrderedDict
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import dash_ag_grid as dag


df = pd.DataFrame(OrderedDict([
    ('plc', ['[S7-1500] Milling', '[M340] Handling', '[S7-400] Sawing', '[S7-1500] Communication']),
    ('tag_name', ["alarm_es", "start", "temp", "watchdog"]),
    ('tag_address', ['%DB25.DBW12', '%M05', '%DB25.DBW18', '%DB25.DBW0'])
]))

# PLC grid
columnDefs = [
    { 'field': 'PLC Name' },
    { 'field': 'PLC Address' },
    { 'field': 'Description' },
    { 'field': 'Watchdog' },
] 
defaultColDef = {'editable': True}

plcs = [
    {"PLC Name": "PLC 1", "PLC Address": "192.168.0.1", "Description": "Description 1", "Watchdog": "DB1.DBW0"},
    {"PLC Name": "PLC 2", "PLC Address": "192.168.0.2", "Description": "Description 2", "Watchdog": ""},
    {"PLC Name": "PLC 3", "PLC Address": "192.168.0.3", "Description": "Description 3", "Watchdog": "DB1.DBW8"},
]

# create a dag.AgGrid with data from plcs
plc_grid = dag.AgGrid(
    id="plc-grid",
    rowData=plcs,
    columnDefs=columnDefs,
    defaultColDef=defaultColDef,
    columnSize="sizeToFit",
)

card_tasks = dbc.Card(
    children=[
        dbc.CardHeader(children="Tasks"),
        dbc.CardBody(
            children=[
                dmc.Accordion(
                    chevronPosition="left",
                    variant="contained",
                    children=[
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Manage PLCs"),
                                dmc.AccordionPanel(
                                    plc_grid
                                ),
                            ],
                            value="manage_plcs",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Add tags manually"),
                                dmc.AccordionPanel(
                                    # Add a dropdown to select the PLC and a button to open a modal
                                    html.Div(
                                        dbc.Row(
                                        [
                                            dbc.Col(dmc.Select(
                                                label="Select PLC:",
                                                description='test',
                                                required=True,
                                                data=["[S7-1500] Milling", "[M340] Handling", "[S7-400] Sawing", "[S7-1500] Communication"],
                                                searchable=True,
                                                nothingFound="No options found",
                                                style={"width": 200},
                                            )),
                                            dbc.Col(dmc.Button(
                                                "Add tags",
                                                leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled"),
                                            ))
                                        ])
                                    ),
                                ),
                            ],
                            value="add_tags_manually",
                        ),
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Import & Export tags"),
                                dmc.AccordionPanel(
                                    "Export the tag list as a csv file, edit it with your favorite spreadsheet editor and import it back."
                                ),
                            ],
                            value="import_export",
                        ),
                    ],
                ),
            ],
        ),
    ],
)





layout = html.Div(
    card_tasks
)


'''
The data table can have the following columns:
 - PLC Name
 - Tag Name
 - Tag address
 - Status (OK, KO, NA)

A PLC has the following (hidden) attributes:
 - Name
 - IP address
 - Job Name
 - Topic Name
 - Polling Interval
 - Heartbeat Address (None if not used)
'''