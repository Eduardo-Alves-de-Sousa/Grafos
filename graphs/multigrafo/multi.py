def multigrafos(graphs):

    multigrafos = []
    #Função para percorrer o Multigrafo
    for graph in graphs:
        edges = set(tuple(edge) for edge in graph['edges'])
        if len(graph['edges']) != len(edges):
            multigrafos.append(graph['id'])
    #pegar os IDs do JSON
    if multigrafos:
        print("IDs dos multigrafos:", multigrafos)
    else:
        print("Desculpe! Nenhum multigrafo foi encontrado")