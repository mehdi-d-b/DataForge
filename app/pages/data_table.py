from dash import Dash, dash_table, html
import pandas as pd
import numpy as np
from collections import OrderedDict
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

plc_names = ["[S7-1500] Milling", "[M340] Handling", "[S7-400] Sawing", "[S7-1500] Communication"]

# PLC grid
PLCcolumnDefs = [
    { 'field': 'PLC Name' , "checkboxSelection": True,"headerCheckboxSelection": True},
    { 'field': 'PLC Address'},
    { 'field': 'Description' },
    { 'field': 'Polling Interval (ms)' },
    { 'field': 'Watchdog' },
] 
PLCdefaultColDef = {'editable': True}

plcs = [
    {"PLC Name": plc_names[0], "PLC Address": "192.168.0.1", "Description": "Description 1", "Watchdog": "DB1.DBW0", "Polling Interval (ms)": 1000},
    {"PLC Name": plc_names[1], "PLC Address": "192.168.0.2", "Description": "Description 2", "Watchdog": "", "Polling Interval (ms)": 500},
    {"PLC Name": plc_names[2], "PLC Address": "192.168.0.3", "Description": "Description 3", "Watchdog": "DB1.DBW8", "Polling Interval (ms)": 100},
]

# create a dag.AgGrid with data from plcs
plc_grid = dag.AgGrid(
    id="plc-grid",
    rowData=plcs,
    columnDefs=PLCcolumnDefs,
    defaultColDef=PLCdefaultColDef,
    columnSize="sizeToFit",
    dashGridOptions={
        "rowSelection": "multiple",
        'undoRedoCellEditing': True,
        'undoRedoCellEditingLimit': 20,
        #"domLayout": "autoHeight"
    }
)

card_tasks = dbc.Card(
    children=[
        dbc.CardHeader(children="📝Tasks"),
        dbc.CardBody(
            children=[
                dmc.Accordion(
                    chevronPosition="left",
                    variant="contained",
                    children=[
                        dmc.AccordionItem(
                            [
                                dmc.AccordionControl("Manage PLCs"),
                                dmc.AccordionPanel([
                                    plc_grid,
                                    dmc.Button("🗑️ Remove Selected", id="btn-rmv-plc", variant="outline"),
                                    dmc.Button("➕ Add PLC", id="btn-add-plc", variant="outline"),
                                ]),
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
                                            dbc.Col("Select PLC:"),
                                            dbc.Col(dmc.Select(
                                                data=["[S7-1500] Milling", "[M340] Handling", "[S7-400] Sawing", "[S7-1500] Communication"],
                                                searchable=True,
                                                nothingFound="No options found",
                                                style={"width": 200},
                                            )),
                                            dbc.Col(dmc.Button(
                                                "Add tag",
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

# PLC grid
TagscolumnDefs = [
    { 'field': 'PLC Name', 'editable' : False, "checkboxSelection": True, "headerCheckboxSelection": True},
    { 'field': 'Tag name' },
    { 'field': 'Description' },
    { 'field': 'Tag address' },
    { 'field': 'Status', 'editable' : False },
] 
TagsdefaultColDef = {'editable': True, "resizable": True, "sortable": True, "filter": True, "columnSize": "responsiveSizeToFit"}

tags = [
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 1", "Description": "Description 1", "Tag address": "DB1.DBW0", "Status": "⚪"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 2", "Description": "Description 2", "Tag address": "DB1.DBW8", "Status": "🟢"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 3", "Description": "Description 3", "Tag address": "DB1.DBW16", "Status": "🟢"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 4", "Description": "Description 4", "Tag address": "DB1.DBW24", "Status": "🟢"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 5", "Description": "Description 5", "Tag address": "DB1.DBW32", "Status": "⚪"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 6", "Description": "Description 6", "Tag address": "DB1.DBW40", "Status": "🟢"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 7", "Description": "Description 7", "Tag address": "DB1.DBW48", "Status": "⚪"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 8", "Description": "Description 8", "Tag address": "DB1.DBW56", "Status": "🟢"},
    {"PLC Name": np.random.choice(plc_names), "Tag name": "Tag 9", "Description": "Description 9", "Tag address": "DB1.DBW64", "Status": "🟢"}, 
]


# create a dag.AgGrid with data from plcs
tag_grid = dag.AgGrid(
    id="tag-grid",
    rowData=tags,
    columnDefs=TagscolumnDefs,
    defaultColDef=TagsdefaultColDef,
    columnSize="sizeToFit",
    dashGridOptions={
        "rowSelection": "multiple",
        'undoRedoCellEditing': True,
        'undoRedoCellEditingLimit': 20
    }
)



card_tags = dbc.Card(
    children=[
        dbc.CardHeader(children="🏷️ Tags"),
        dbc.CardBody(
            children=[
                tag_grid,
                dmc.Button("🗑️ Remove Selected", id="btn-rmv-tag", variant="outline"),
                dmc.Button("➕ Add Tag", id="btn-add-tag", variant="outline"),
            ],
        ),
    ],
)



layout = html.Div([
    card_tasks,
    html.Br(),
    card_tags,
    html.Br(),
    dmc.Affix(
        dmc.Button("💾 Save Changes"), position={"bottom": 20, "right": 20}
    )
]
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