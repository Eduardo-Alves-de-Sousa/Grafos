import json
import sys

class Grafo:
    def __init__(self, graph_data):
        self.id = graph_data['id']
        self.vertices = graph_data['vertices']
        self.arestas = graph_data['arestas']

    def is_multigrafo(self):
        return len(self.arestas) > len(set(self.arestas))

    def is_pseudografo(self):
        return len(self.arestas) != len(set(self.arestas))

    def is_conectado(self):
        visited = set()
        stack = [self.vertices[0]]

        while stack:
            current_vertex = stack.pop()
            visited.add(current_vertex)

            for edge in self.arestas:
                if current_vertex in edge:
                    neighbor = edge[0] if edge[1] == current_vertex else edge[1]
                    if neighbor not in visited:
                        stack.append(neighbor)

        return len(visited) == len(self.vertices)

    def is_completo(self):
        num_vertices = len(self.vertices)
        num_arestas_completas = num_vertices * (num_vertices - 1) // 2
        return len(self.arestas) == num_arestas_completas

    def get_grau_vertice(self, vertex):
        return sum(1 for edge in self.arestas if vertex in edge)

    def __str__(self):
        return f"Grafo {self.id}"

class Grafos:
    def __init__(self):
        self.grafos = []

    def carregar_de_json(self, nome_arquivo):
        with open(nome_arquivo) as arquivo:
            dados = json.load(arquivo)
            self.grafos = [Grafo(graph_data) for graph_data in dados['grafos']]
    
    def executar_comando(self, comando):
        partes = comando.strip().split(' ')
        if partes[0] == 'carregar':
            if len(partes) == 2:
                self.carregar_de_json(partes[1])
            else:
                print("Comando inválido. Uso: carregar <nome_arquivo>")
        elif partes[0] == 'multigrafos':
            for grafo in self.grafos:
                if grafo.is_multigrafo():
                    print(f"{grafo} é um multigrafo")
            if not any(grafo.is_multigrafo() for grafo in self.grafos):
                print("Não existem multigrafos")
        elif partes[0] == 'pseudografos':
            for grafo in self.grafos:
                if grafo.is_pseudografo():
                    print(f"{grafo} é um pseudografo")
            if not any(grafo.is_pseudografo() for grafo in self.grafos):
                print("Não existem pseudografos")
        elif partes[0] == 'desconectados':
            for grafo in self.grafos:
                if not grafo.is_conectado():
                    print(f"{grafo} é desconectado")
        elif partes[0] == 'completos':
            for grafo in self.grafos:
                if grafo.is_completo():
                    print(f"{grafo} é completo")
        elif partes[0] == 'grau':
            if len(partes) == 3:
                id_grafo = int(partes[1])
                vertice = partes[2]
                grafo_encontrado = next((grafo for grafo in self.grafos if grafo.id == id_grafo), None)
                if grafo_encontrado:
                    grau = grafo_encontrado.get_grau_vertice(vertice)
                    if grau is not None:
                        print(f"Grau do vértice {vertice} no grafo {grafo_encontrado}: {grau}")
                    else:
                        print(f"Vértice {vertice} não encontrado no grafo {grafo_encontrado}")
                else:
                    print(f"Grafo não encontrado: {id_grafo}")
            else:
                print("Comando inválido. Uso: grau <id_grafo> <vertice>")
        elif partes[0] == 'info':
            if len(partes) == 2:
                id_grafo = int(partes[1])
                grafo_encontrado = next((grafo for grafo in self.grafos if grafo.id == id_grafo), None)
                if grafo_encontrado:
                    print(f"Informações do grafo {grafo_encontrado.id}:")
                    print(f"Número de vértices do grafo: {len(grafo_encontrado.vertices)}")
                    print(f"Número de arestas do grafo: {len(grafo_encontrado.arestas)}")
                    print(f"Conectado: {grafo_encontrado.is_conectado()}")
                    print(f"Completo: {grafo_encontrado.is_completo()}")
                else:
                    print(f"Desculpe!! Grafo não encontrado: {id_grafo}")
            else:
                print("Comando inválido. Uso: info <id_grafo>")
        elif partes[0] == 'sair':
            sys.exit()
        else:
            print("Comando inválido")
#Cria uma instância da classe Grafos e inicia um loop para receber 
#os comandos de analise do grafo desejado. Comando é passado para o 
#método executar_comando para ser processado
def main():
    grafos = Grafos()
    while True:
        comando = input("Digite um comando: ")
        grafos.executar_comando(comando)

if __name__ == '__main__':
    main()


'''Um multigrafo é um grafo que contém múltiplas arestas entre os mesmos pares de vértices.
   Um pseudografo é um grafo que contém laços, ou seja, arestas que conectam um vértice a ele mesmo.
   Um grafo é considerado desconectado se houver pelo menos um vértice que não pode ser alcançado a partir de outros vértices.
   Um grafo completo é um grafo no qual cada par de vértices é conectado por uma aresta. 
   O grau de um vértice é o número de vezes em que ele ocorre como extremo de uma aresta.
   Um vértice é considerado alcançável se houver um caminho (uma sequência de arestas) que o conecte a partir de algum outro vértice do grafo.
   um vértice é considerado inalcançável se não houver nenhum caminho que o conecte a partir de qualquer outro vértice do grafo.
   BFS (Busca em Largura) e DFS (Busca em Profundidade) são dois algoritmos de busca utilizados em grafos para percorrer ou buscar elementos no grafo.'''