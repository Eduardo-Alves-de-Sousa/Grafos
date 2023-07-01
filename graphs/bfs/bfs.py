def bfs(graphs, graph_id, start_vertex, end_vertex):
    for graph in graphs:
        if graph['id'] == graph_id:
            vertices = graph['vertices']
            edges = graph['edges']
            visited = {vertex: False for vertex in vertices}
            queue = [(start_vertex, [start_vertex])]
            while queue:
                current_vertex, path = queue.pop(0)
                visited[current_vertex] = True
                if current_vertex == end_vertex:
                    print(f"Caminho encontrado no grafo {graph_id}: {' -> '.join(path)}")
                    return
                queue.extend((adj_vertex, path + [adj_vertex])
                             for edge in edges
                             for adj_vertex in edge
                             if current_vertex in edge and not visited[adj_vertex])
            break
    print(f"Nenhum caminho encontrado para o grafo {graph_id} entre {start_vertex} e {end_vertex}")
