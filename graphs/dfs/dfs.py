def dfs(graphs, graph_id, start_vertex, end_vertex):
    found_graph = False
    for graph in graphs:
        if graph['id'] == graph_id:
            found_graph = True
            vertices = graph['vertices']
            edges = graph['edges']
            start_vertex = start_vertex.strip('"')
            end_vertex = end_vertex.strip('"')
            visited = {vertex: False for vertex in vertices}
            stack = [(start_vertex, [start_vertex])]
            while stack:
                current_vertex, path = stack.pop()
                visited[current_vertex] = True
                if current_vertex == end_vertex:
                    print(f"Caminho encontrado para o grafo foi{graph_id}: {' -> '.join(path)}")
                    break
                for edge in edges:
                    next_vertex = edge[1] if edge[0] == current_vertex else edge[0]
                    if not visited[next_vertex]:
                        stack.append((next_vertex, path + [next_vertex]))
            else:
                print("Desculpe, mas nenhum caminho foi encontrado para grafo {graph_id} entre {start_vertex} e {end_vertex}")
            break
    if not found_graph:
        print("Desculpe! O grafo não foi encontrado:", graph_id)