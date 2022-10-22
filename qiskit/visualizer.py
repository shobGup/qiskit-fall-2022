from .graph import Graph
# from PIL import Image
import pydot

# [1: [1, 2, 3, 4]]
def display(graph_data):
    graph_viz = pydot.Dot(graph_type="directed")
    graph_viz.set_label("Link Graph")

    # insert vertices
    for v in graph_data:
        vertex = pydot.Node(v)
        vertex.set_style("filled")
        vertex.set_fillcolor("#b2cede")
        graph_viz.add_node(vertex)

    # insert directed edges
    for start_vert in graph_data:
        for end_vert in start_vert:
            edge = pydot.Edge(start_vert, end_vert)
            graph_viz.add_edge(edge)
    
    graph_viz.write_png('graph_output.png')
    