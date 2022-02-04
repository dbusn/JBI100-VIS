from datetime import date
from dash import dcc, html
from ..config import final, attributes_heat, cities_df


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Visualization of Traffic Accidents in the UK"),
            html.Div(
                id="intro",
                children="Choose the attributes of your interest",
            ),
        ],
    )


def generate_control_card(isHeatMap):
    """

    :return: A Div containing controls for graphs.
    """
    if isHeatMap is True:
        return html.Div(
            id="control-card",
            children=[
                html.H6("Tools for the HeatMap View: "),
                html.Br(),
                html.Label("Select Attribute:"),
                dcc.Dropdown(
                    id="select-z-attribute-dropdown",
                    options=[{"label": i.replace("_", " "), "value": i} for i in attributes_heat],
                    value=attributes_heat[0],
                ),
                html.Br(),
                html.Label('Select City:'),
                dcc.Dropdown(
                    id="city-selection-dropdown",
                    options=[{"label": entry, "value": entry} for entry in cities_df['city'].tolist()],
                    value='Hunshelf',
                ),
            ],
            style={"textAlign": "float-left"}
        )
    else:
        return html.Div(
            id="control-card",
            children=[
                html.H6("Tools for the Chart View: "),
                dcc.DatePickerRange(
                    id='date-picker-range',
                    min_date_allowed=date(2015, 1, 1),
                    max_date_allowed=date(2015, 12, 31),
                    initial_visible_month=date(2015, 1, 1),
                    start_date=date(2015, 1, 1),
                    end_date=date(2015, 12, 31)
                ),
                html.Br(),
                html.Br(),
                html.Label("Common x Attribute"),
                dcc.Dropdown(
                    id="select-x-attribute-bar-1",
                    options=[{"label": i.replace("_", " "), "value": i} for i in final],
                    value=final[0],
                ),
                html.Br(),
                html.Label("Attribute Grouping the 1st Graph"),
                dcc.Dropdown(
                    id="select-x-attribute-bar-2",
                    options=[{"label": i.replace("_", " "), "value": i} for i in final],
                    value=final[1],
                ),
                html.Br(),
                html.Label("Attribute Grouping the 2nd Graph (Only in the Graph with 3 Categorical Attributes)"),
                dcc.Dropdown(
                    id="select-x-attribute-bar-3",
                    options=[{"label": i.replace("_", " "), "value": i} for i in final],
                    value=final[2],
                ),
                html.Br(),
                html.Label("Showing in Amount or Percentage (Only in the Graph with 3 Categorical Attributes)"),
                dcc.Dropdown(
                    id="amount-or-percent",
                    options=[{"label": 'Amount', "value": 'Amount'}, {"label": 'Percentage', "value": 'Percentage'}],
                    value="Amount",
                ),
            ], style={"textAlign": "float-left"}
        )


def make_menu_layout(isHeatMap):
    return [generate_description_card(), generate_control_card(isHeatMap)]
