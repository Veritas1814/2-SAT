import networkx as nx
import matplotlib.pyplot as plt
# from original_graph import OG
from testing import G as OG
from copy import copy

def assign_numbers_to_nodes(OG):
    res = {}
    i = 1
    for node in OG.nodes:
        res[node] = i
        i += 1
    G = nx.relabel_nodes(OG, res, copy=True)
    return G, res

def add_color(G, node, color):
    if color not in G.nodes[node]['colors']:
        G.nodes[node]['colors'].append(color)
        remove_color(G, -node, color)

def remove_color(G, node, color):
    if color in G.nodes[node]['colors']:
        G.nodes[node]['colors'].remove(color)
        if len(G.nodes[node]['colors']) == 0:
            raise ValueError('Graph is not colorable')
        if len(G.nodes[node]['colors']) == 1:
            for neigh in G[node]:
                add_color(G, neigh, G.nodes[node]['colors'][0])

def create_implementation_graph(OG:nx.Graph):
    Imp_G = nx.Graph() 
    nodes = list(OG.nodes) + [-a for a in OG.nodes]
    Imp_G.add_nodes_from(nodes)
    for edge in OG.edges:
        Imp_G.add_edge(edge[0], -edge[1])
        Imp_G.add_edge(edge[1], -edge[0])

    for node in Imp_G.nodes:
        if node > 0:
            Imp_G.nodes[node]['colors'] = ['blue', 'green', 'red']
        else:
            Imp_G.nodes[node]['colors'] = []
            add_color(Imp_G, node, OG.nodes[-node]['color'])
    return Imp_G
    
def is_valid(Imp_G):
    #dfs here
    pass 

def choose_colors(Imp_G: nx.Graph):
    for node in Imp_G.nodes:
        if node > 0:
            if len(Imp_G.nodes[node]['colors']) != 1:
                possible_colors = []
                for neigh in Imp_G[node]:
                    possible_colors += list(Imp_G.nodes[neigh]['colors'])
                opt_1, opt_2 = tuple(Imp_G.nodes[node]['colors'])
                
                opt_1_count = possible_colors.count(opt_1)
                opt_2_count = possible_colors.count(opt_2)

                if opt_1_count < opt_2_count:
                    remove_color(Imp_G, node, opt_1)
                elif opt_1_count > opt_2_count:
                    remove_color(Imp_G, node, opt_2)
        else:
            break

    return Imp_G

def color_and_return_pairs(OG):
    res = []
    G, mapping = assign_numbers_to_nodes(OG)
    Imp_G = create_implementation_graph(G)
    Colored_Imp_G = choose_colors(Imp_G)
    mapping = {mapping[node]: node for node in mapping}
    for node in Colored_Imp_G.nodes:
        if node > 0:
            res.append((mapping[node], Colored_Imp_G.nodes[node]['colors'][0]))
        else:
            break
    return res

def color_and_return_graph(OG:nx.Graph):
    New_G = copy(OG)
    G, mapping = assign_numbers_to_nodes(OG)
    Imp_G = create_implementation_graph(G)
    Colored_Imp_G = choose_colors(Imp_G)

    for node in New_G.nodes:
        New_G.nodes[node]['color'] = Colored_Imp_G.nodes[mapping[node]]['colors'][0]

    return New_G


# New_G = color_and_return_graph(OG)
# subax1 = plt.subplot(121)
# nx.draw(New_G, with_labels=True, font_weight='bold')
# plt.show()

print(color_and_return_pairs(OG))

