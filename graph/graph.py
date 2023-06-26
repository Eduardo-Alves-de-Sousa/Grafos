class Graph:

    def __init__(self, json):
        self.__input = json
        self.__graph = {}
        self.adj_mtx = []