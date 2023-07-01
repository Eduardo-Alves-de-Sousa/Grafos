import json
import sys

class Grafos:
    #O método __init__ inicializa a lista de grafos.
    def __init__(self):
        self.grafos = []
    #Carrega os grafos a partir de um arquivo JSON.
    def ler_json(self, nome_arquivo):
        with open(nome_arquivo) as arquivo:
            # função "json.load" para carregar diretamente o arquivo JSON
            dados = json.load(arquivo)
            self.grafos = dados['grafos']
    #Verifica se há multigrafos na lista de grafos
    def possui_multigrafos(self):
        possui_multigrafo = any(len(g['arestas']) > len(set(g['arestas'])) for g in self.grafos)
        if possui_multigrafo:
            print("Existem multigrafos")
        else:
            print("Não existem multigrafos")
    #Verifica se há pseudografos na lista de grafos
    def possui_pseudografos(self):
        possui_pseudografo = any(len(g['arestas']) != len(set(g['arestas'])) for g in self.grafos)
        if possui_pseudografo:
            print("Existem pseudografos")
        else:
            print("Não existem pseudografos")
    def possui_grafos_completos(self):
        for i, grafo in enumerate(self.grafos):
            vertices = grafo['vertices']
            arestas = grafo['arestas']
            num_vertices = len(vertices)
            num_arestas_completas = num_vertices * (num_vertices - 1) // 2
            if len(arestas) == num_arestas_completas:
                print(f"O grafo {i} é completo")
    '''percorre a lista de grafos, verifica se o grafo é conectado usando o método e_conectado
       diretamente ligado com o desconexo'''
    def e_conectado(self, vertices, arestas):
        adjacencias = {v: set() for v in vertices}
        for aresta in arestas:
            u, v = aresta
            adjacencias[u].add(v)
            adjacencias[v].add(u)

        visitados = set()
        pilha = [vertices[0]]
        while pilha:
            v = pilha.pop()
            visitados.add(v)
            for u in adjacencias[v]:
                if u not in visitados:
                    pilha.append(u)

        return len(visitados) == len(vertices)
    #Obtém o grau de um vértice em um determinado grafo. 
    #Ele recebe o ID do grafo e o vértice desejado como entrada
    def obter_grau_vertice(self, id_grafo, vertice):
        grafo_encontrado = next((g for g in self.grafos if g['id'] == id_grafo), None)
        if grafo_encontrado:
            graus = {v: 0 for v in grafo_encontrado['vertices']}
            for aresta in grafo_encontrado['arestas']:
                if aresta[0] in graus:
                    graus[aresta[0]] += 1
                if aresta[1] in graus:
                    graus[aresta[1]] += 1
            if vertice in graus:
                print(f"Grau do vértice {vertice} no grafo {id_grafo}: {graus[vertice]}")
            else:
                print(f"Vértice {vertice} não encontrado no grafo {id_grafo}")
        else:
            print(f"Grafo não encontrado: {id_grafo}")
    #Percorre as informações dos grafos contidos no arquivo JSON
    def obter_informacoes_grafo(self, id_grafo):
        grafo_encontrado = next((g for g in self.grafos if g['id'] == id_grafo), None)
        if grafo_encontrado:
            num_vertices = len(grafo_encontrado['vertices'])
            num_arestas = len(grafo_encontrado['arestas'])
            e_conectado = self.e_conectado(grafo_encontrado['vertices'], grafo_encontrado['arestas'])
            e_completo = len(grafo_encontrado['arestas']) == num_vertices * (num_vertices - 1) // 2
            print(f"Informações do grafo desejado{id_grafo}:")
            print(f"Número de vértices do grafo: {num_vertices}")
            print(f"Número de arestas do grafo: {num_arestas}")
            print(f"verificando se é Conectado: {e_conectado}")
            print(f"Verificando se é Completo: {e_completo}")
        else:
            print(f"Desculpe!! Grafo não encontrado: {id_grafo}")
    #Analisa um comando inserido pelo usuário e chama os métodos 
    #correspondentes para executar a operação desejada.
    def executar_comando(self, comando):
        partes = comando.strip().split(' ')
        if partes[0] == 'carregar':
            if len(partes) == 2:
                self.carregar_de_json(partes[1])
            else:
                print("Comando inválido. Uso: carregar <nome_arquivo>")
        elif partes[0] == 'multigrafos':
            self.possui_multigrafos()
        elif partes[0] == 'pseudografos':
            self.possui_pseudografos()
        elif partes[0] == 'desconectados':
            self.possui_grafos_desconectados()
        elif partes[0] == 'completos':
            self.possui_grafos_completos()
        elif partes[0] == 'grau':
            if len(partes) == 3:
                id_grafo = int(partes[1])
                vertice = partes[2]
                self.obter_grau_vertice(id_grafo, vertice)
            else:
                print("Comando inválido. Uso: grau <id_grafo> <vertice>")
        elif partes[0] == 'info':
            if len(partes) == 2:
                id_grafo = int(partes[1])
                self.obter_informacoes_grafo(id_grafo)
            else:
                print("Comando inválido. Uso: info <id_grafo>")
        elif partes[0] == 'sair':
            sys.exit()
        else:
            print("Comando inválido")
#Cria uma instância da classe Grafos e inicia um loop para receber 
#os comandos de analise do grafo desejado. Comando é passado para o 
#método executar_comando para ser processado.
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