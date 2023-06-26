import graph.graph as gi

def menu_inicial():
    print("Menu de Opções: \n")
    print("1º Verificar Multigrafos")
    print("2º Verificar Pseudografos")
    print("3º Verificar Grafos Desconexos")
    print("4º Verificar Grafos Completos")
    print("5º Verificar Pseudografos")
    print("6º Verificar Graus de Um Grafo")
    print("7º Verificar Vertices Alcançaveis de Um Grafo")
    print("8º Verificar Vertices Inalcançaveis de Um Grafo")
    print("9º Verificar Vertices Inalcançaveis de Um Grafo")
    print("10º Algoritmo BFS no Grafo")
    print("11º Algoritmo DFS no Grafo")

def selecao(op):
    if op == 1 or op == "1":
        pass
    elif op == 2 or op == "2":
        pass
    elif op == 3 or op == "3":
        pass
    elif op == 4 or op == "4":
        pass
    elif op == 5 or op == "5":
        pass
    elif op == 6 or op == "6":
        pass
    elif op == 7 or op == "7":
        pass
    elif op == 8 or op == "8":
        pass
    elif op == 9 or op == "9":
        pass
    elif op == 10 or op == "10":
        pass
    elif op == 11 or op == "11":
        pass
    else:
        print("Opção inválida")




#import functions.is_multgraph.multigraph as mtg

if __name__ == "__main__":
    
    print("-------------------------")
    print("*   Teoria dos Grafos   *")
    print("-------------------------")
    print("1º Vamos carregar o arquivo json\n")
    try:
        # input do arquivo
        data = input("Digite o nome do arquivo sem o .json: ")
        print("\n")
    except KeyboardInterrupt:
        print("\n")
        print("Entrada não informada")
        exit(1)

    # Chamada de função que faz a desserialização JSON
    graph = gi.Graph(f"{data}.json")

    menu_inicial()

    op = input("Selecione a opção que deseja prosseguir: ")

    print("\n")
   # mtg.is_multigraph()
    # multigrafh, pseudograph, completegraph, desconex = graph.graph_check()

    # print(f"É multigrafo: {multigrafh}")
    # print(f"É pseudografo: {pseudograph}")
    # print(f"É desconexo: {desconex}")
    # print(f"É grafo completo: {completegraph}")

    # graus = graph.graus_vertices()
    # print(f"Grau dos Vértices do id=1: {graus}")

    # a_grau = graph.degree_vertice_input("A")
    # print(f"Grau do Vértice A do id=1: {a_grau}")

    # vertice_a = graph.reachable_vertices_of_A(1, "A")
    # print(f"Vértices alcançavéis de A: {vertice_a}")
    
    # vertice_ina = graph.vertices_unreachable_of_A(1, "A")
    # print(f"Vértices inalcançavéis de A: {vertice_ina}")
    # print(graph.bfs_graph("A", "BV"))

    # print(graph.dfs("A", "H"))