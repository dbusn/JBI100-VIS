import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc

from ..config import cities_df


# Heatmap class containing and managing  object of the heatmap figure
class MapViewHeat(html.Div):
    # Read the dataset
    df = pd.read_csv('https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/jbi100_app/datasets/dataset_heatmap.csv')
    df.astype('float')

    # Initialize the figure
    fig = go.Figure(go.Densitymapbox(lat=df.Latitude, lon=df.Longitude,
                                     hovertext="", hoverinfo="text", radius=5, opacity=0.5))

    # Layout settings
    fig.update_layout(mapbox_style="carto-darkmatter", mapbox_center_lat=51, mapbox_center_lon=0, width=1095,
                      height=650)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    fig.update_mapboxes(zoom=6)

    current_city = 'Brighton'

    # Updates the z-attribute of the heatmap
    def update_z_attr(self, attr):
        self.fig.update_traces(z=self.df[attr])
        return self.fig

    # Updates the viewport of the heatmap
    def update_heatmap_area(self, city):
        self.current_city = city
        cities_df.astype('str')
        city_row = cities_df.loc[cities_df['city'] == city]
        self.fig.update_mapboxes(center_lat=city_row.iloc[0]['latitude'], center_lon=city_row.iloc[0]['longitude'],
                                 zoom=11)

    # Constructor
    def __init__(self, name):
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="map-heat-class",
            children=[
                # TODO Change the size of the graph
                dcc.Graph(figure=self.fig, id=self.html_id)
            ],
        )
