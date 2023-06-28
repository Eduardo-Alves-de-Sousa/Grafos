from collections import defaultdict
import graph.ler_grafo as gm

class Graph:
    def __init__(self, json):
        self.__input = json
        self.__graph = {}
        self.adj_mtx = []

    def graph_check(self):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        mult, pseud, complet, desconex = {}, {}, {}, {}

        for i in range(len(self.__graph)):
            mult[i + 1] = self.is_multigraph(self.__graph[i]["edges"])
            pseud[i + 1] = self.is_pseudograph(self.__graph[i]["edges"])
            complet[i + 1] = self.is_complete_graph(self.__graph[i]["vertices"], self.__graph[i]["edges"])
            desconex[i + 1] = self.is_disconnected_graph(self.__graph[i]["vertices"], self.__graph[i]["edges"])

        return mult, pseud, complet, desconex
    
    def is_multigraph(self, edges):
        # Criar um dicionário para armazenar as arestas
        edge_dict = defaultdict(int)

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            edge_dict[edge_tuple] += 1
        
        for count in edge_dict.values():
            if count > 1:
                return True
            
        return False
    
    def is_pseudograph(self, edges):
        for edge in edges:
            if edge[0] == edge[1]:
                return True
            
        return False

    def is_disconnected_graph(self, vertices, edges):
        calc = len(vertices) * 2
        if len(edges) * 2 < calc:
            return True
        
        return False

    # verificar se o grafo é completo
    def is_complete_graph(self, vertices, edges):
        calc_edge = (len(vertices) ** 2) - len(vertices)

        if self.is_multigraph(edges) or self.is_pseudograph(edges):
            return False
        elif calc_edge == (len(edges)) * 2 or calc_edge == ((len(edges) - 1) * 2):
            return True
        elif len(edges) % 2 == 0:
            par = calc_edge == len(edges) * 2
            return par
        
        return False

    def graus_vertices(self):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[0]["vertices"]
        edges = self.__graph[0]["edges"]

        edge_dict = defaultdict(int)
        graus = {}

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            edge_dict[edge_tuple] += 1

        for ver in degrees:
            graus[ver] = 0

        for edge, count in edge_dict.items():
            for vertex in graus.keys():
                if vertex in edge:
                    graus[vertex] += count

        return graus

    def degree_vertice_input(self, degree):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degree = self.__graph[0]["vertices"]
        edges = self.__graph[0]["edges"]

        edge_dict = defaultdict(int)
        grau = {}

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            edge_dict[edge_tuple] += 1

        grau[degree] = 0

        for edge, count in edge_dict.items():
            for vertex in grau.keys():
                if vertex in edge:
                    grau[vertex] += count

        return grau

    def reachable_vertices_of_A(self, idgraph, degree):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degree = self.__graph[idgraph]["vertices"]
        edges = self.__graph[idgraph]["edges"]

        edge_dict = defaultdict(int)
        vertex_list = []

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            edge_dict[edge_tuple] += 1

        for edge, count in edge_dict.items():
            if degree in edge and count == 1:
                vertex = edge[0] if edge[0] != degree else edge[1]
                vertex_list.append(vertex)

        return vertex_list

    def vertices_unreachable_of_A(self, idgraph, degree):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degree = self.__graph[idgraph]["vertices"]
        edges = self.__graph[idgraph]["edges"]

        edge_dict = defaultdict(int)
        vertex_list = []

        for edge in edges:
            edge_tuple = tuple(sorted(edge))
            edge_dict[edge_tuple] += 1

        for edge, count in edge_dict.items():
            if degree not in edge and count == 1:
                vertex_list.extend(edge)

        return vertex_list

    def bfs_graph(self, initial, final):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degree = self.__graph[10]["vertices"]
        edges = self.__graph[10]["edges"]

        graph_dict = defaultdict(list)
        for edge in edges:
            graph_dict[edge[0]].append(edge[1])

        visited = set()
        queue = []

        queue.append(initial)
        visited.add(initial)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=", ")

            if vertex == final:
                break

            for neighbor in graph_dict[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfs_function(self, initial, final, visited, graph_dict):
        visited.add(initial)
        print(initial, end=" ")

        if initial == final:
            return True

        for neighbor in graph_dict[initial]:
            if neighbor not in visited:
                if self.dfs_function(neighbor, final, visited, graph_dict):
                    return True

        return False
    
    def dfs(self, initial, final):
        json_file = gm.JsonToDict(self.__input)
        self.__graph = json_file.json_to_graph()["graphs"]
        degrees = self.__graph[10]["vertices"]
        edges = self.__graph[10]["edges"]

        graph_dict = defaultdict(list)
        for edge in edges:
            graph_dict[edge[0]].append(edge[1])

        visited = set()
        self.dfs_function(initial, final, visited, graph_dict)