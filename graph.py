import networkx as nx
import matplotlib.pyplot as plt
import random

def draw_graph(number_of_genes, adjacency_matrix, number_of_color, solution):
    # create networkx graph
    G=nx.Graph()
    #The nodes and edges for draw_graph
    nodes = [x for x in range(number_of_genes)]
    edges = []
    for i in range(number_of_genes):
        for j in range(number_of_genes):
            if j > i and adjacency_matrix[j][i] == 1:
                edges.append((i, j))

    #The colors of nodes
    color =[]
    while len(color) < number_of_color:
        color_value = "#%06x" % random.randint(0, 0xFFFFFF)
        if color_value not in color:
            color.append(color_value)
    color_map=dict(list(enumerate(color)))
    node_color=[color_map[node] for node in solution]
    #The colors of edges 
    color_edges = []
    for i in range(len(edges)):
        if node_color[edges[i][0]] == node_color[edges[i][1]]:
            color_edges.append('#ff7226')
        else:
            color_edges.append('#cfc2cf') 
    #add nodes
    for node in nodes:
        G.add_node(node)
    # add edges
    for edge in edges:
        G.add_edge(edge[0], edge[1])

    # There are graph layouts like shell, spring, spectral and random.
    # Shell layout usually looks better, so we're choosing it.
    # I will show some examples later of other layouts
    graph_pos = nx.shell_layout(G)

    # draw nodes, edges and labels

    nx.draw_networkx_nodes(G, graph_pos, node_size=500, node_color=node_color, alpha=0.8)
    nx.draw_networkx_edges(G, graph_pos, edge_color = color_edges)
    nx.draw_networkx_labels(G, graph_pos, font_size=12, font_family='sans-serif')

    # show graph
##  nx.draw(G, graph_pos, node_color=[color_map[node] for node in node_color], with_labels=True)
    plt.show()  
