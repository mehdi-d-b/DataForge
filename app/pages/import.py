# This page uses a dmc.Stepper component to display the different steps of the import process, which are:
# 1. Download the csv file from the web app (with a button "Download")
# 2. Edit the csv file (this is just for information, the user can edit the file with Excel or any other software)
# 3. Upload the csv file to the web app (with a button "Upload")

from dash_extensions.enrich import dcc, html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc


min_step = 0
max_step = 3
active = 0


upload_button = dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Glisser-déposer ou ',
            html.A('Sélectionner les fichiers')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'display': 'none'
        },
        # Allow multiple files to be uploaded
        multiple=False
    )

checklist = html.Div(
    [
        dmc.Stepper(
            id="stepper-upload-file",
            active=active,
            breakpoint="sm",
            children=[
                dmc.StepperStep(
                    label="Step 1",
                    description="Download the csv template.",
                    children=dmc.Text(
                        "The template contains the columns that are essential to the import process.", align="center"
                    ),
                ),
                dmc.StepperStep(
                    label="Step 2",
                    description="Edit the csv file.",
                    children=dmc.Text(
                        "Open the csv file with your preferred software (for example, Microsoft Excel) and add the tags you want to monitor.", align="center"
                        ),
                ),
                dmc.StepperStep(
                    label="Step 3",
                    description="Upload the csv file.",
                    children=dmc.Text(
                        "Upload the file so the application can update the worker with your new tag informations.", align="center"
                    ),
                ),
                dmc.StepperCompleted(
                    children=dmc.Text(
                        "The import process is complete! You can now access, edit your data in the following table.",
                        align="center",
                    )
                ),
            ],
        ),
        dmc.Group(
            position="center",
            mt="xl",
            children=[
                dmc.Button("Back", id="back-basic-usage", variant="default"),
                dmc.Button("Next", id="next-basic-usage"),
                upload_button
            ],
        ),
    ]
)