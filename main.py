#!/user/bin/python3
import json
import sys

# Importando todas as funções e classes da pasta "graphs"
from graphs.multigrafo.multi import multigrafos
from graphs.pseudografo.pseud import pseudografo
#from graphs.inalcancaveis.inal import inalcancaveis
from graphs.graus.graus import graus
from graphs.grau.grau import grau
from graphs.dfs.dfs import dfs
#from graphs.desconexos.desconect import desconect
from graphs.completos.completo import completo
from graphs.bfs.bfs import bfs
#from graphs.alcancaveis.alcanca import alcancaveis

#Classe principal
class GraphsMain:
    def __init__(self):
        self.graphs = []

    def ler_json(self, filename):
        try:
            with open(filename, 'r') as file:
                # função "json.load" para carregar diretamente o arquivo JSON
                data = json.load(file) 
                self.graphs = data.get('graphs', [])
                print(f"Arquivo '{filename}' carregado com sucesso!")
        except FileNotFoundError:
            print("Desculpe!! Seu arquivo JSON não foi encontrado:", filename)
    '''Aplicando comandos para percorrer o arquivo JSON já carregado, 
       em busca dos devidos GRAFOS espeficados pelos comando'''
    def handle_command(self, command):
        cmd, *args = command  

        if cmd == 'abrir' and len(args) == 2 and args[0] == 'arquivo':
            self.ler_json(args[1])

        elif cmd == 'identificar_grafos_multigrafos':
            multigrafos(self.graphs)

        elif cmd == 'identificar_grafos_pseudografos':
            pseudografo(self.graphs)

        elif cmd == 'identificar_grafos_completos':
            completo(self.graphs)

        elif cmd == 'identificar_graus' and len(args) == 1:
            graph_id = int(args[0].split('=')[1])
            graus(self.graphs, graph_id)

        elif cmd == 'identificar_grau' and len(args) == 2:
            graph_id = int(args[0].split('=')[1])
            vertex = args[1].split('=')[1].strip('"')
            grau(self.graphs, graph_id, vertex)

        elif cmd == 'identificar_grafos_bfs' and len(args) == 3:
            graph_id = int(args[0].split('=')[1])
            start_vertex = args[1].split('=')[1].strip('"')
            end_vertex = args[2].split('=')[1].strip('"')
            bfs(self.graphs, graph_id, start_vertex, end_vertex)

        elif cmd == 'identificar_grafos_dfs' and len(args) == 3:
            graph_id = int(args[0].split('=')[1])
            start_vertex = args[1].split('=')[1].strip('"')
            end_vertex = args[2].split('=')[1].strip('"')
            dfs(self.graphs, graph_id, start_vertex, end_vertex)

        elif cmd == 'sair':
            confirm = input("Deseja realmente sair? (s/n)")
            if confirm.lower() == 's':
                sys.exit()

        else:
            print("Comando inválido")
    '''Método "run()" para iniciar a execução da classe principal,
       criando um loop para espera dos comando dos grafos'''
    def run(self):
        while True:
            user_input = input()
            command = user_input.split()
            self.handle_command(command)

#Função MAIN para verificação do arquivo JSON que foi executado
if __name__ == '__main__':
    graph_tool = GraphsMain()
    graph_tool.run()
