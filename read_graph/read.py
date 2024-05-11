import csv
import networkx as nx
# import matplotlib.pyplot as plt
def read_table(filename):
    G = nx.Graph()
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for i,row in enumerate(csv_reader):
            if i ==0:
                continue
            vertex1, vertex2, color1, color2 = row
            G.add_node(vertex1,color=f"{color1}")
            G.add_node(vertex2,color=f"{color2}")
            G.add_edge(vertex1, vertex2)
    return G

# def draw_graph(G):
#     node_colors = [G.nodes[node]['color'] for node in G.nodes()]
#     nx.draw(G, with_labels=True, node_color=node_colors)
#     plt.show()
# graph = read_table("table.csv")
# draw_graph(graph)