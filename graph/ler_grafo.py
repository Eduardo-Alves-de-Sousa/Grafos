import json

class JsonToDict:
    def __init__(self, input_file):
        self.__input = input_file
        self.__data = {}
    
    def json_to_graph(self):
        with open(self.__input) as json_file:
            self.__data = json.load(json_file)
        return self.__data