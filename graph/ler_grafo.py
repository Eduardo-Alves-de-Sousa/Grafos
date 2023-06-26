import json

class JsonToDict:
    def __init__(self, input):
        self.__input = input
        self.__data = {}
    
    def json_to_graph(self):
        with open(self.__input) as json_file:
            self.__data = json.load(json_file)
        return self.__data