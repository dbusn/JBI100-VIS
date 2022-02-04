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

    def update(self, feature_x_1, feature_x_2, type, month):
        self.fig = go.Figure()

        # Create a list that stores all traces
        traces = []
        # Normal bar chart when only 1 categorical attribute is given
        if feature_x_1 == feature_x_2:
            temp = self.df[[feature_x_2, 'Month']]
            # Filter off rows with unknown value
            if month != 'All':
                temp = temp[temp['Month'] == month]
            temp = temp[temp[feature_x_2] != '100000000']
            temp = temp[temp[feature_x_2] != 100000000]
            # Count number of accidents grouped by 1 attribute
            temp = temp.groupby(feature_x_2).size()
            temp = temp.rename('Size').reset_index()
            trace = go.Bar(name=feature_x_2, x=temp[feature_x_2], y=temp['Size'])
            # Append all bars in horizontal direction
            traces.append(trace)
        # Stacked bar chart when only 1 categorical attribute is given
        else:
            temp = self.df[[feature_x_1, feature_x_2, 'Month']]
            if month != 'All':
                temp = temp[temp['Month'] == month]
            # Filter off rows with unknown value
            temp = temp[(temp[feature_x_2] != '100000000') & (temp[feature_x_1] != '100000000')]
            temp = temp[(temp[feature_x_2] != 100000000) & (temp[feature_x_1] != 100000000)]
            # Count number of accidents grouped by 2 attributes
            temp = temp.groupby([feature_x_2, feature_x_1]).size()
            temp = temp.rename('Size').reset_index()
            # Append all bars in horizontal direction first, and then in vertical direction to form stacked bar chart
            for i in temp[feature_x_2].unique():
                trace = go.Bar(name=str(i), x=temp[temp[feature_x_2] == i][feature_x_1],
                               y=temp[temp[feature_x_2] == i]['Size'])
                traces.append(trace)

        for i in range(len(traces)):
            self.fig.add_trace(traces[i])
        self.fig.update_layout(
            yaxis_zeroline=False,
            xaxis_zeroline=False,
            barmode='stack',
        )
        # Show the items in percentage based on attribute
        # Otherwise show the items in the absolute amount
        if type == "Percentage":
            self.fig.update_layout(
                barnorm='percent',
            )

        # Add titles of x-axis, y-axis and legend
        self.fig.update_layout(
            xaxis_title=feature_x_1.replace("_", " "),
            yaxis_title="Number of Accidents",
            legend_title=feature_x_2.replace("_", " "),
        )

        # Add the main title of the graph
        if feature_x_1 == feature_x_2:
            self.fig.update_layout(
                title_text='Number of Accidents with ' + feature_x_2.replace("_", " ") + ' (' + type + ')',
            )
        else:
            self.fig.update_layout(
                title_text='Number of Accidents with ' + feature_x_1.replace("_", " ") +
                           ' Grouped by ' + feature_x_2.replace("_", " ") + ' (' + type + ')',
            )

        return self.fig

    def reload_df(self, df):
        self.df = df
