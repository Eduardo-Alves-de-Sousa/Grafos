def grau(graphs, graph_id, vertex):
    for graph in graphs:
        if graph['id'] == graph_id:
            edges = graph['edges']
            degree = 0

            for edge in edges:
                if vertex in edge:
                    degree += 1

            print("O grau do vértice", vertex, "no grafo", graph_id, "é", degree)
            return
    print("Desculpe! O grafo não foi encontrado:", graph_id)