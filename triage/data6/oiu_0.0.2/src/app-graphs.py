from ogdf_python import ogdf, cppinclude
import pandas as pd
cppinclude("ogdf/planarity/PlanarizationLayout.h")
cppinclude("ogdf/basic/graphics.h")


global default_colors
default_colors = {
    'red': ogdf.Color(r=245, g=20, b=20, a=204),
    'green': ogdf.Color(r=20, g=200, b=20, a=204),
    'blue': ogdf.Color(r=0, g=40, b=245, a=204),
    'yellow': ogdf.Color(r=245, g=245, b=0, a=204),
    'purple': ogdf.Color(r=70, g=0, b=200, a=204),
    'pink': ogdf.Color(r=200, g=0, b=140, a=204),
    'orange': ogdf.Color(r=245, g=100, b=0, a=204),
    'brown': ogdf.Color(r=100, g=40, b=0, a=204),
    'gray': ogdf.Color(r=120, g=120, b=120, a=204),
    'light_green': ogdf.Color(r=100, g=245, b=100, a=204),
    'light_blue': ogdf.Color(r=40, g=140, b=245, a=204),
    'light_red': ogdf.Color(r=245, g=60, b=60, a=204),
    'dark_green': ogdf.Color(r=0, g=90, b=0, a=204),
    'dark_blue': ogdf.Color(r=0, g=30, b=60, a=204),
    'dark_red': ogdf.Color(r=90, g=0, b=0, a=204)
}


class graph():
    def __init__(self):
        self.G = ogdf.Graph()
        self.GA = ogdf.GraphAttributes(self.G, ogdf.GraphAttributes.all)

    def read(self,
             filename_apps,
             apps_sheet_name,
             filename_interfaces,
             interfaces_sheet_name,
             apps,
             components,
             source,
             target,
             interface_direction,
             technologies,
             colors=None
             ):

        self.colors = colors

        self.df_app = pd.read_excel(filename_apps, engine='openpyxl',
                                    sheet_name=apps_sheet_name, header=None).dropna(how='all')
        self.df_app.dropna(axis=1, how='all', inplace=True)
        self.df_app.columns = self.df_app.iloc[0]
        self.df_app = self.df_app.iloc[1:].reset_index(drop=True)

        self.df_int = pd.read_excel(filename_interfaces, engine='openpyxl',
                                    sheet_name=interfaces_sheet_name, header=None).dropna(how='all')
        self.df_int.dropna(axis=1, how='all', inplace=True)
        self.df_int.columns = self.df_int.iloc[0]
        self.df_int = self.df_int.iloc[1:].reset_index(drop=True)

        apps_column = self.df_app.columns.values.tolist()

        if apps not in apps_column:
            print(
                f"Column {apps} in {filename_apps}, on sheet {apps_sheet_name} does not exist.")
            return

        if components not in apps_column:
            print(
                f"Column {components} in {filename_apps}, on sheet {apps_sheet_name} does not exist.")
            return

        if colors and colors not in apps_column:
            print(
                f"Column {colors} in {filename_apps}, on sheet {apps_sheet_name} does not exist.")
            return

        int_column = self.df_int.columns.values.tolist()

        if source not in int_column:
            print(
                f"Column {source} in {filename_interfaces}, on sheet {interfaces_sheet_name} does not exist.")
            return

        if target not in int_column:
            print(
                f"Column {target} in {filename_interfaces}, on sheet {interfaces_sheet_name} does not exist.")
            return

        if interface_direction not in int_column:
            print(
                f"Column {interface_direction} in {filename_interfaces}, on sheet {interfaces_sheet_name} does not exist.")
            return

        if technologies not in int_column:
            print(
                f"Column {technologies} in {filename_interfaces}, on sheet {interfaces_sheet_name} does not exist.")
            return

        optionsRight = ['>', '->', '-->', '--->', '---->', 'desno', 'right']
        optionsLeft = ['<', '<-', '<--', '<---', '<----', 'levo', 'left']

        for i in range(len(self.df_int)):
            if pd.isnull(self.df_int[interface_direction][i]):
                continue
            elif str(self.df_int[interface_direction][i]).lower() in optionsRight:
                self.df_int[interface_direction][i] = 'forward'
            elif str(self.df_int[interface_direction][i]).lower() in optionsLeft:
                self.df_int[interface_direction][i] = 'back'
            else:
                self.df_int[interface_direction][i] = 'both'

        self.df_app.rename(
            columns={apps: 'apps', components: 'components'}, inplace=True)
        if colors:
            self.df_int.rename(columns={colors: 'colors'}, inplace=True)

        self.df_int.rename(columns={source: 'source', target: 'target',
                           interface_direction: 'interface_direction', technologies: 'technologies'}, inplace=True)

    def draw(self):
        j = -1
        # adding apps, components as edges and edges between app and it's components.
        app = None
        NODES = {}
        b = None
        for i in range(self.df_app.shape[0]):
            if pd.isnull(self.df_app['apps'][i]) == False:
                j = j + 1
                j = j % 15
                app = self.df_app['apps'][i]
                node = self.G.newNode()
                self.GA.label[node] = app
                self.GA.width[node] = 7 * len(app)
                NODES[app] = node

                if self.colors:
                    color = self.df_app['colors'][i]
                    if pd.isnull(self.df_app['apps'][i]):
                        b = default_colors['gray']
                    if color in default_colors:
                        b = default_colors[color]
                    else:
                        h = color.lstrip('#')
                        r, g, b = [int(h[i:i+2], 16) for i in [0, 2, 4]]
                        b = ogdf.Color(r=r, g=g, b=b, a=204)
                else:
                    b = list(default_colors.items())[j][1]
                self.GA.fillColor[node] = b
                self.GA.strokeWidth[node] = 2

            elif app and pd.isnull(self.df_app['components'][i]) == False:
                podaplikacija = self.df_app['components'][i]
                node = self.G.newNode()
                self.GA.label[node] = podaplikacija
                self.GA.width[node] = 7 * len(podaplikacija)
                NODES[podaplikacija] = node
                self.GA.fillColor[node] = b
                self.GA.strokeWidth[node] = 0
                edge = self.G.newEdge(NODES[app], node)
                self.GA.strokeColor[edge] = b
                self.GA.strokeWidth[edge] = 2
                self.GA.arrowType[edge] = 0

        # adding interfaces, each interface is represented with node and two edges.

        for i in range(self.df_int.shape[0]):
            if pd.isnull(self.df_int['source'][i]) == False and pd.isnull(self.df_int['target'][i]) == False:
                node = self.G.newNode()
                self.GA.shape[node] = ogdf.Shape.Ellipse
                if pd.isnull(self.df_int['technologies'][i]) == False:
                    self.GA.label[node] = self.df_int['technologies'][i]
                    self.GA.width[node] = 10 * \
                        len(self.df_int['technologies'][i])
                if self.df_int['interface_direction'][i] == 'forward':
                    edge1 = self.G.newEdge(
                        NODES[self.df_int['source'][i]], node)
                    edge2 = self.G.newEdge(
                        node, NODES[self.df_int['target'][i]])
                elif self.df_int['interface_direction'][i] == 'back':
                    edge1 = self.G.newEdge(
                        node, NODES[self.df_int['source'][i]])
                    edge2 = self.G.newEdge(
                        NODES[self.df_int['target'][i]], node)
                else:
                    edge1 = self.G.newEdge(
                        node, NODES[self.df_int['source'][i]])
                    edge2 = self.G.newEdge(
                        NODES[self.df_int['target'][i]], node)
                    edgeArrow = ogdf.EdgeArrow.Both
                    self.GA.arrowType[edge1] = edgeArrow
                    self.GA.arrowType[edge2] = edgeArrow

        # calling planarization layout algorithm on graph

        PL = ogdf.PlanarizationLayout()
        PL.call(self.GA)

    def save_svg(self, filename):
        ogdf.GraphIO.write(self.GA, filename+".svg", ogdf.GraphIO.drawSVG)
