def graus(graphs, graph_id):
    graph = next((g for g in graphs if g['id'] == graph_id), None)
    if graph is None:
        print("Desculpe! O grafo não foi encontrado:", graph_id)
        return

    vertices = graph['vertices']
    edges = graph['edges']
    degrees = {vertex: 0 for vertex in vertices}

    for vertex in vertices:
        for edge in edges:
            if vertex in edge:
                degrees[vertex] += 1

    print(f"Os graus dos vértices para o grafo {graph_id}:")
    for vertex, degree in degrees.items():
        print("Vértice:", vertex, "Grau:", degree)
