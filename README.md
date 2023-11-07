# Custo uniforme ou Dijkstra de grafo de larga escala

• Estende a BUSCA EM LARGURA de modo a encontrar a solução ótima para
qualquer valor de passo
• Estratégia: expandir nó com menor custo de caminho g(n)
• Fronteira = fila ordenada pelo g(n)
• Alteração em relação à busca em largura:
	– Teste de objetivo: feito quando um nó é selecionado para expansão
(e não quando é criado) => no Pop(frontier)
	– Se o nó já está na fronteira, mesmo assim é necessário verificar se o
caminho encontrado é mais barato que aquele guardado

## Pseudocode
```
procedure uniform_cost_search(start) is
    node ← start
    frontier ← priority queue containing node only
    expanded ← empty set
    do
        if frontier is empty then
            return failure
        node ← frontier.pop()
        if node is a goal state then
            return solution(node)
        expanded.add(node)
        for each of node's neighbors n do
            if n is not in expanded and not in frontier then
                frontier.add(n)
            else if n is in frontier with higher cost
                replace existing node with n
```

#### Leia mais
Mais info.: https://courses.cs.washington.edu/courses/csep573/14sp/slides/2_BlindSearch.pdf
