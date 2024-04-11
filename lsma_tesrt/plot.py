import plotly.express as px


class Plot:

    def __init__(self, clusters, projections):
        self.clusters = clusters
        self.projections = projections
        self.labels = [(i+1, i+1) for ind, i in enumerate(clusters.labels_)]
        self.colors = px.colors.qualitative.Plotly
        self.fig = None

    def create_plot(self):
        print('Creating plot.')
        self.fig = px.scatter(
            self.projections, x=0, y=1,marginal_y="violin",
           marginal_x="box", trendline="ols",
            color=self.labels, color_discrete_sequence=self.colors, labels={'color': 'species'}
        )

    def show(self):
        print('Show plot.')
        self.fig.show()

    def save(self, path: str = 'images/fig.png'):
        self.fig.write_image(path)
