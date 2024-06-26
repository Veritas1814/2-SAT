import networkx as nx 
import random
from itertools import combinations, groupby
import matplotlib.pyplot as plt




def gnp_random_connected_graph(n, p):
    """
    Generates a random undirected graph, similarly to an Erdős-Rényi 
    graph, but enforcing that the resulting graph is conneted
    """
    edges = combinations(range(n), 2)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    if p <= 0:
        return G
    if p >= 1:
        return nx.complete_graph(n, create_using=G)
    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        G.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < p:
                G.add_edge(*e)
    #Part until here was taken from 1 lab in this semester

    for node in G.nodes():
        G.nodes[node]['color'] = random.choice(['red', 'green', 'blue'])

    return G

nodes = random.randint(10,100)
probability = 0.01
G = gnp_random_connected_graph(nodes,probability)

plt.figure(figsize=(8, 6))
nx.draw(G, node_color = [G.nodes[node]['color'] for node in G.nodes()],
        with_labels=True)
plt.show()
