def dfs(graphs, graph_id, start_vertex, end_vertex):
    for graph in graphs:
        if graph['id'] == graph_id:
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

                stack.extend((next_vertex, path + [next_vertex]) for edge in edges for next_vertex in (edge[1], edge[0]) if edge[0] == current_vertex or edge[1] == current_vertex and not visited[next_vertex])

            print(f"Desculpe, mas nenhum caminho foi encontrado para o grafo {graph_id} entre {start_vertex} e {end_vertex}")
            return
    print("Desculpe! O grafo não foi encontrado:", graph_id)
