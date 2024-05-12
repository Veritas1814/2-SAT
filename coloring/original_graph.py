import networkx as nx
import matplotlib.pyplot as plt

OG = nx.Graph()


OG.add_nodes_from([(11, {'color':'red'}),
                   (21, {'color':'blue'}),
                   (31, {'color':'green'}),
                   (41, {'color':'green'}),
                   (51, {'color':'red'}),
                   (61, {'color':'blue'}),
                   (71, {'color':'green'}),
                   (81, {'color':'red'})])

OG.add_edges_from([
    (11, 21), (21, 31), (21, 41), (31, 41), (11, 41), (11, 81), 
    (41, 51), (41, 71), (51, 61), (61, 71), (71, 81), (11, 31)
])



# # OG = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(OG, with_labels=True, font_weight='bold')
# plt.show()


