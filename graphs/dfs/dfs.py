def dfs(graphs, graph_id, start_vertex, end_vertex):
    graph = next((g for g in graphs if g['id'] == graph_id), None)
    if graph is None:
        print("Desculpe! O grafo não foi encontrado:", graph_id)
        return

    vertices = graph['vertices']
    edges = graph['edges']
    start_vertex, end_vertex = start_vertex.strip('"'), end_vertex.strip('"')
    visited = {vertex: False for vertex in vertices}
    stack = [(start_vertex, [start_vertex])]

    while stack:
        current_vertex, path = stack.pop()
        visited[current_vertex] = True

        if current_vertex == end_vertex:
            print(f"Caminho encontrado para o grafo {graph_id}: {' -> '.join(path)}")
            return

        adjacent_vertices = [next_vertex for edge in edges for next_vertex in edge if current_vertex in edge and not visited[next_vertex]]
        stack.extend((next_vertex, path + [next_vertex]) for next_vertex in adjacent_vertices)

    print(f"Desculpe, mas nenhum caminho foi encontrado para o grafo {graph_id} entre {start_vertex} e {end_vertex}")
