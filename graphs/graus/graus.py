def graus(graphs, graph_id):
    #found_graph = False

    for graph in graphs:
        if graph['id'] == graph_id:
            #found_graph = True
            vertices = graph['vertices']
            edges = graph['edges']
            degrees = {vertex: 0 for vertex in vertices}

            for edge in edges:
                degrees[edge[0]] += 1
                degrees[edge[1]] += 1

            print("Os graus dos vértices para o grafo")
            for vertex, degree in degrees.items():
                print("Vértice:", vertex, "Grau:", degree)
            
            return

    print("Desculpe! O grafo não foi encontrado:", graph_id)