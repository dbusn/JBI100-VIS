import plotly.graph_objects as go
from dash import dcc, html


class Barplot(html.Div):
    def __init__(self, name, df):
        self.html_id = name.lower().replace(" ", "-")
        self.df = df

        # Equivalent to `html.Div([...])`
        super().__init__(
            className="graph_card",
            children=[
                html.H6(name),
                dcc.Graph(id=self.html_id)
            ],
        )

    def update(self, feature_x_1, feature_x_2):
        self.fig = go.Figure()

        traces = []
        if feature_x_1 == feature_x_2:
            temp = self.df[[feature_x_1]]
            temp = temp[temp[feature_x_1]!='100000000']
            temp = temp[temp[feature_x_1]!=100000000]
            temp = temp.groupby(feature_x_1).size()
            temp = temp.rename('Size').reset_index()
            trace = go.Bar(name=feature_x_1, x=temp[feature_x_1], y=temp['Size'])
            traces.append(trace)
        else:
            temp = self.df[[feature_x_1, feature_x_2]]
            temp = temp[(temp[feature_x_1]!='100000000')&(temp[feature_x_2]!='100000000')]
            temp = temp[(temp[feature_x_1]!=100000000)&(temp[feature_x_2]!=100000000)]
            temp = temp.groupby([feature_x_1, feature_x_2]).size()
            temp = temp.rename('Size').reset_index()
            for i in temp[feature_x_1].unique():
                trace = go.Bar(name=str(i), x=temp[temp[feature_x_1]==i][feature_x_2], y=temp[temp[feature_x_1]==i]['Size'])
                traces.append(trace)
        
        for i in range(len(traces)):
            self.fig.add_trace(traces[i])
        self.fig.update_layout(
            yaxis_zeroline=False,
            xaxis_zeroline=False,
            barmode='stack',
        )

        self.fig.update_layout(
            xaxis_title=feature_x_2.replace("_", " "),
            yaxis_title="Number of Accidents",
            legend_title=feature_x_1.replace("_", " "),
        )

        if feature_x_1 == feature_x_2:
            self.fig.update_layout(
                title_text='Number of Accidents with ' + feature_x_1.replace("_", " "),
            )
        else:
            self.fig.update_layout(
                title_text='Number of Accidents with ' + feature_x_2.replace("_", " ") + ' Grouped by ' + feature_x_1.replace("_", " "),
            )

        return self.fig
