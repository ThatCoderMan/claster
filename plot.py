import plotly.express as px


class Plot:

    def __init__(self, clusters, projections):
        self.clusters = clusters
        self.projections = projections
        self.labels = [i+1 for i in clusters.labels_]
        self.colors = ...
        self.fig = None

    def create_plot(self):
        print('Creating plot.')
        self.fig = px.scatter(
            self.projections, x=0, y=1,
            color=self.labels, color_discrete_sequence=self.colors, labels={'color': 'species'}
        )

    def show(self):
        print('Show plot.')
        self.fig.show()

    def save(self, path: str = 'images/fig.png'):
        self.fig.write_image(path)
