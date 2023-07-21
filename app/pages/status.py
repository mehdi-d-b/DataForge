from dash import html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

kafka_card = dmc.Card(
    children=[
        dmc.Group(
            [
                dmc.Text("Streaming Platform", weight=500),
                dmc.Badge("Online", color="teal", variant="filled", id="kafka-status-badge"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "💡 Apache Kafka is an Open Source Streaming Platform. It's in charge of collecting data and pushing it to the database.",
            size="sm",
            color="dimmed",
        ),
        dmc.Button(
            "↗ Open interface",
            variant="light",
            color="blue",
            fullWidth=True,
            mt="md",
            radius="md",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

db_card = dmc.Card(
    children=[
        dmc.Group(
            [
                dmc.Text("Database", weight=500),
                dmc.Badge("Offline", color="gray", variant="filled", id="db-status-badge"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "💡 QuestDB is an Open Source database specialized for timeseries. It's the fastest and most efficient if you want to store lots and lots of data!",
            size="sm",
            color="dimmed",
        ),
        dmc.Button(
            "↗ Open interface",
            variant="light",
            color="blue",
            fullWidth=True,
            mt="md",
            radius="md",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

app_card = dmc.Card(
    children=[
        dmc.Group(
            [
                dmc.Text("App", weight=500),
                dmc.Badge("Online", color="teal", variant="filled"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "💡 This is the whole application statistics",
            size="sm",
            color="dimmed",
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 350},
)

layout = html.Div([
    dbc.Row(
            [
                dbc.Col(kafka_card),
                dbc.Col(db_card),
                dbc.Col(app_card),
            ]
        ),
])
