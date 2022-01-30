import pandas as pd
import plotly.figure_factory as ff
from dash import html, dcc


class MapViewHex(html.Div):
    df = pd.read_csv('https://raw.githubusercontent.com/dbusn/JBI100-VIS/main/dataset_unique.csv')

    df['Latitude'] = df['Latitude'].astype(float)
    df['Longitude'] = df['Longitude'].astype(float)

    fig = ff.create_hexbin_mapbox(
        data_frame=df, lat="Latitude", lon="Longitude",
        nx_hexagon=20, opacity=0.5, labels={"color": "Accident Count"},
        min_count=1, color_continuous_scale="Viridis",
        show_original_data=True,
        original_data_marker=dict(size=2, opacity=0.1, color="deeppink")
    )
    fig.update_layout(mapbox_style="carto-darkmatter", mapbox_center_lat=51, mapbox_center_lon=0, width=1095,
                      height=650)
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    def __init__(self, name):
        self.html_id = name.lower().replace(" ", "-")

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="map-hex-class",
            children=[
                dcc.Graph(figure=self.fig)
            ],
        )
