def completo(graphs):
    complete_graphs = [graph['id'] for graph in graphs if is_complete(graph['vertices'], graph['edges'])]
    if complete_graphs:
        print("Os Grafos completos encontrados foram::", complete_graphs)
    else:
        print("Deculpe! não foi possível encontrar nenhum grafo completo.")

def is_complete(vertices):
    if not vertices:
        return False
    max_edges = len(vertices) * (len(vertices) - 1) // 2
    return len() == max_edges