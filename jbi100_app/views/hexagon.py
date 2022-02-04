import pandas as pd
import plotly.figure_factory as ff
from dash import html, dcc

from ..config import cities_df


# Class containing the hexmap object
class MapViewHex(html.Div):
    # Read the data
    df = pd.read_csv('https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/jbi100_app/datasets/dataset_unique.csv')
    current_city = 'Brighton'

    # Convert DataFrame type to float
    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)

    # Define the figure
    fig = ff.create_hexbin_mapbox(
        data_frame=df, lat="Latitude", lon="Longitude",
        nx_hexagon=20, opacity=0.5, labels={"color": "Accident Count"},
        min_count=1, color_continuous_scale="Viridis",
        show_original_data=True,
        original_data_marker=dict(size=2, opacity=0.1, color="deeppink")
    )

    # Layout updates
    fig.update_layout(mapbox_style="carto-darkmatter", mapbox_center_lat=51, mapbox_center_lon=0, width=1095,
                      height=650)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    # Update the viewport of the hexmap
    def update_hexmap_area(self, city):
        self.current_city = city
        cities_df.astype('str')
        city_row = cities_df.loc[cities_df['city'] == city]
        self.fig.update_mapboxes(center_lat=city_row.iloc[0]['Latitude'], center_lon=city_row.iloc[0]['Longitude'],
                                 zoom=11)
        return self.fig

    # Constructors
    def __init__(self, name):
        self.current_city = 'Brighton'
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="map-hex-class",
            children=[
                dcc.Graph(figure=self.fig)
            ],
        )
