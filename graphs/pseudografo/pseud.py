def pseudografo(graphs):
    pseudografo = []

    for graph in graphs:
        vertices = graph['vertices']
        edges = graph['edges']

        if any(edge[0] == edge[1] and edge[0] in vertices for edge in edges):
            pseudografo.append(graph['id'])

    if pseudografo:
        print("IDs dos pseudografos:", pseudografo)
    else:
        print("Desculpe! Nenhum pseudografo foi encontrado")