import graph.graph as gi

def menu_inicial():
    print("Menu de Opções:\n")
    print("1. Verificar Multigrafos")
    print("2. Verificar Pseudografos")
    print("3. Verificar Grafos Desconexos")
    print("4. Verificar Grafos Completos")
    print("5. Verificar Graus de Um Grafo")
    print("6. Verificar Vertices Alcançaveis de Um Grafo")
    print("7. Verificar Vertices Inalcançaveis de Um Grafo")
    print("8. Algoritmo BFS no Grafo")
    print("9. Algoritmo DFS no Grafo")

def selecao(op, graph):
    if op == "1":
        mult, pseud, complet, desconex = graph.graph_check()
        print("Multigrafos:", mult)
    elif op == "2":
        mult, pseud, complet, desconex = graph.graph_check()
        print("Pseudografos:", pseud)
    elif op == "3":
        mult, pseud, complet, desconex = graph.graph_check()
        print("Grafos Desconexos:", desconex)
    elif op == "4":
        mult, pseud, complet, desconex = graph.graph_check()
        print("Grafos Completos:", complet)
    elif op == "5":
        graus = graph.graus_vertices()
        print("Graus de Um Grafo:", graus)
    elif op == "6":
        idgraph = int(input("Digite o ID do grafo: "))
        degree = int(input("Digite o grau do vértice: "))
        vertices_alcancaveis = graph.reachable_vertices_of_A(idgraph, degree)
        print("Vertices Alcançaveis de Um Grafo:", vertices_alcancaveis)
    elif op == "7":
        idgraph = int(input("Digite o ID do grafo: "))
        degree = int(input("Digite o grau do vértice: "))
        vertices_inalcancaveis = graph.vertices_unreachable_of_A(idgraph, degree)
        print("Vertices Inalcançaveis de Um Grafo:", vertices_inalcancaveis)
    elif op == "8":
        initial = int(input("Digite o vértice inicial: "))
        final = int(input("Digite o vértice final: "))
        bfs_result = graph.bfs_graph(initial, final)
        print("Resultado do Algoritmo BFS:", bfs_result)
    elif op == "9":
        initial = int(input("Digite o vértice inicial: "))
        final = int(input("Digite o vértice final: "))
        dfs_result = graph.dfs(initial, final)
        print("Resultado do Algoritmo DFS:", dfs_result)
    else:
        print("Opção inválida")

if __name__ == "__main__":
    print("-------------------------")
    print("*   Teoria dos Grafos   *")
    print("-------------------------")
    print("1. Vamos carregar o arquivo JSON\n")
    try:
        # Input do arquivo
        data = input("Digite o nome do arquivo sem a extensão .json: ")
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

    selecao(op, graph)