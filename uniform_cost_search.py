#!/usr/bin/python3
""" Busca de custo uniforme """
from node import Node


def uniform_cost_search(graph, start, goal):
    """ Funcao de busca de custo uniforme

        Args:
            graph
            start (str): inicio
            goal (str): fim ou estado objectivo

        Return:
            caminho ou None
    """
    a_explorar = []
    start_node = Node(state=start, parent=None, action=None, cost=0)
    a_explorar.append(start_node)
    explorados = set()

    while a_explorar:
        a_explorar.sort(key=lambda x: x.cost)
        node = a_explorar.pop(0)

        if node.state == goal:
            caminho = []
            while node:
                caminho.insert(0, node.state)
                node = node.parent
            return (caminho)

        if node.state not in explorados:
            explorados.add(node.state)
            for vizinho, cost in graph[node.state]:
                filho = Node(
                        state=vizinho, parent=node,
                        action=vizinho, cost=node.cost + cost)
                a_explorar.append(filho)

    return (None)
