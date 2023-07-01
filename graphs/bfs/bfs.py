from collections import deque

def bfs(graphs, graph_id, start_vertex, end_vertex):
    graph = next((g for g in graphs if g['id'] == graph_id), None)
    if graph is None:
        print(f"Desculpe! O grafo {graph_id} não foi encontrado.")
        return

    vertices = graph['vertices']
    edges = graph['edges']
    visited = {vertex: False for vertex in vertices}
    queue = deque([(start_vertex, [start_vertex])])

    while queue:
        current_vertex, path = queue.popleft()

        if current_vertex == end_vertex:
            print(f"Caminho encontrado no grafo {graph_id}: {' -> '.join(path)}")
            return

        if visited[current_vertex]:
            continue

        visited[current_vertex] = True

        adjacent_vertices = [adj_vertex for edge in edges for adj_vertex in edge if current_vertex in edge]
        queue.extend((adj_vertex, path + [adj_vertex]) for adj_vertex in adjacent_vertices)

    print(f"Nenhum caminho encontrado para o grafo {graph_id} entre {start_vertex} e {end_vertex}")
