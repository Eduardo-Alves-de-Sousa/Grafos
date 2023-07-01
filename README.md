# Trabalho avaliativo de Grafos
-Trabalho de criação de GRAFOS, lendo arquivo JSON

## Implementar uma ferramenta chamada "grafos" com intereface em linha de comando. Abaixo estão exemplo de chamadas da ferramenta:

* grafos carrregar arquivo.json //deve carregar os grafos contidos no arquivo .json
* grafos multigrafos //deve informar quais grafos do arquivo carregado são multigrafos
* grafos pseudografos //deve informar quais grafos do arquivo carregado são pseudografos
* grafos desconexos //deve informar quais grafos do arquivo carregado são desconexos
* grafos completos //deve informar quais grafos do arquivo carregado são completos
* grafos graus id=1 //deve informar quais os graus dos vértices do grafo de id=1
* grafos grau id=1 vertice="A"  //deve informar o grau do vértice=A do grafo id=1 
* grafos alcancaveis partida="A"  //deve informar quais vértices do grafo são alcançáveis a partir do *vértice = A
* grafos inalcancaveis partida="A" //deve informar quais vértices do grafo são inalcançáveis a partir do *vértice = A
* grafos bfs partida="A" chegada="B" //deve informar o caminho partindo do vértice = A até chegar no *vértice=B usando o algoritmo BFS.
* grafos dfs partida="A" chegada="B" //deve informar o caminho partindo do vértice = A até chegar no *vértice=B usando o algoritmo DFS.
* grafos sair // finaliza a execução da ferramenta

### O que foi feito!!.
- Foi criado toda construção dos graficos faltando apenas os grafos (a criação de um executavel funcional, grafos alcancaveis, grafos desconexos, grafos inalcancaveis).
- Toda criação dos demais grafos está situada na pasta "graphs".
- Criação de uma classe principal chamada "main.py" onde contém todos os importes dos grafos feitos, a leitura do arquivo .JSON, apresenta também os comandos para percorrer o arquivo JSON (desde o carregar arquivo.json, até o comando "sair")fazendo as buscas dos devidos grafos solicitados, inclusive apresenta uma função "main" para verificação do JSON.
- 
