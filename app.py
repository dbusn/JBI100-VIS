from dash import html, dcc
from dash.dependencies import Input, Output

from jbi100_app.data import get_data
from jbi100_app.main import app
from jbi100_app.views.barplot import Barplot
from jbi100_app.views.heatmap import MapViewHeat
from jbi100_app.views.hexagon import MapViewHex
from jbi100_app.views.menu import make_menu_layout

# TODO add documentation

# Create data
df = get_data()

# Instantiate custom views
barplot_0 = Barplot("barplot-1", df)
barplot_1 = Barplot("barplot-2", df)
barplot_2 = Barplot("barplot-3", df)
barplot_3 = Barplot("barplot-4", df)
mapViewHex = MapViewHex("hexmap")
mapViewHeat = MapViewHeat("heatmap")

# Define layout
app.layout = html.Div(
    id="app-container",
    children=[
        # Left column: Define menu in app
        html.Div(
            id="left-column",
            className="three columns",
            children=make_menu_layout(False)
        ),

        # Right column: Define 4 tabs/pages in app
        html.Div(
            id="right-column",
            className="nine columns",
            children=[
                dcc.Tabs(
                    id='tab-aggregator',
                    value='chart-view',
                    children=[
                        dcc.Tab(label='Bar Chart View (With 2 Categorical Attributes)', value='chart-view'),
                        dcc.Tab(label='Bar Chart View (With 3 Categorical Attributes)', value='chart-2-view'),
                        dcc.Tab(label='Hexmap View', value='hex-view'),
                        dcc.Tab(label='Heatmap View', value='heat-view')
                    ]
                ),
                # TODO make it fill the rest of the page
                html.Div(id='tabs-content')
            ],
        ),
    ],
)

# Generate barplot-1 in the 1st page of app
@app.callback(
    Output("barplot-1", "figure"),
    Input("select-x-attribute-bar-1", "value"),
    Input("select-x-attribute-bar-2", 'value'),
    # Input("date-picker-range", "start_date"),
    # Input("date-picker-range", "end_date"),
)
def update_0(feature_x_1, feature_x_2):
    # df = update_date(start_date, end_date)
    # barplot_0.reload_df(df)
    return barplot_0.update(feature_x_1, feature_x_2, "Amount")

# Generate barplot-2 in the 1st page of app
@app.callback(
    Output("barplot-2", "figure"),
    Input("select-x-attribute-bar-1", "value"),
    Input("select-x-attribute-bar-2", 'value'),
    # Input("date-picker-range", "start_date"),
    # Input("date-picker-range", "end_date"),
)
def update_1(feature_x_1, feature_x_2):
    # df = update_date(start_date, end_date)
    # barplot_1.reload_df(df)
    return barplot_1.update(feature_x_1, feature_x_2, "Percentage")

# Generate barplot-3 in the 2nd page of app
@app.callback(
    Output("barplot-3", "figure"),
    Input("select-x-attribute-bar-1", "value"),
    Input("select-x-attribute-bar-2", 'value'),
    Input("amount-or-percent", 'value'),
    # Input("date-picker-range", "start_date"),
    # Input("date-picker-range", "end_date"),
)
def update_2(feature_x_1, feature_x_2, type):
    # df = update_date(start_date, end_date)
    # barplot_2.reload_df(df)
    return barplot_2.update(feature_x_1, feature_x_2, type)

# Generate barplot-4 in the 2nd page of app
@app.callback(
    Output("barplot-4", "figure"),
    Input("select-x-attribute-bar-1", "value"),
    Input("select-x-attribute-bar-3", 'value'),
    Input("amount-or-percent", 'value'),
    # Input("date-picker-range", "start_date"),
    # Input("date-picker-range", "end_date"),
)
def update_3(feature_x_1, feature_x_3, type):
    # df = update_date(start_date, end_date)
    # barplot_3.reload_df(df)
    return barplot_3.update(feature_x_1, feature_x_3, type)

# Generate menu on the left side of the app
@app.callback(
    Output('tabs-content', 'children'),
    Output('left-column', 'children'),
    Input('tab-aggregator', 'value')
)

# Update menu based on the type of chart/view chosen
def update_view(tab):
    if tab == 'chart-view':
        return html.Div([barplot_0, barplot_1]), make_menu_layout(False)
    elif tab == 'chart-2-view':
        return html.Div([barplot_2, barplot_3]), make_menu_layout(False)
    elif tab == 'heat-view':
        return html.Div([mapViewHeat]), make_menu_layout(True)
    else:
        return html.Div([mapViewHex]), make_menu_layout(False)

@app.callback(
    Output('heatmap', 'figure'),
    Input('select-z-attribute-dropdown', 'value'),
    Input('city-selection-dropdown', 'value')
)
def update_heatmap(attr, city):
    if city != mapViewHeat.current_city:
        mapViewHeat.update_heatmap_area(city)

    return mapViewHeat.update_z_attr(attr)


if __name__ == '__main__':
    app.run_server(debug=False, dev_tools_ui=False, use_reloader=True)

