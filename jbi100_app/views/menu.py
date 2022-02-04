from dash import dcc, html

from ..config import final, attributes_heat, cities_df, months_list


def generate_description_card():
    """

    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Visualization of Traffic Accidents in 2015 in the UK"),
            html.Div(
                id="intro",
            ),
        ],
    )


def generate_control_card(viewType):
    """

    :return: A Div containing controls for graphs.
    """
    if viewType == 'heat-view':
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
                    value='Brighton',
                ),
            ],
            style={"textAlign": "float-left"}
        )
    elif viewType == 'chart-view' or viewType == 'chart-2-view':
        return html.Div(
            id="control-card",
            children=[
                html.H6("Tools for the Chart View: "),
                html.Br(),
                html.Label('Select month range:'),
                dcc.Dropdown(
                    id='month-selector-dropdown',
                    options=[{"label": i.replace("_", " "), "value": i} for i in months_list],
                    value=months_list[0]
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
            ],
            style={"textAlign": "float-left"}
        )
    elif viewType == 'hex-view':
        return html.Div(
            id="control-card",
            children=[
                html.H6("Tools for the HexMap View: "),
                html.Br(),
                html.Label('Select City:'),
                dcc.Dropdown(
                    id="hex-city-selection-dropdown",
                    options=[{"label": entry, "value": entry} for entry in cities_df['city'].tolist()],
                    value='Brighton',
                ),
            ],
            style={"textAlign": "float-left"}
        )


def make_menu_layout(viewType):
    return [generate_description_card(), generate_control_card(viewType)]
