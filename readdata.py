def load_data(path, number_of_genes):
    edges = []
    with open(path, mode='r') as f:
        for line in f.readlines():
            _, w1, w2 = line.split()
            if w1 != w2:
                edges.append((int(w1)-1, int(w2)-1))

    adjacency_matrix = [[0 for x in range(number_of_genes)] for x in range(number_of_genes)]
    for edge in edges:
        adjacency_matrix[edge[1]][edge[0]] = 1

    return adjacency_matrix
