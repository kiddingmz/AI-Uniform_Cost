#!/usr/bin/python
""" Representacao do No no Grafo """


class Node:
    """ A class No """
    def __init__(self, state, parent, action, cost):
        """ Inicializacao do constructor

        Args:
            state (str): estado do no
            parent (Node ou None): no pai
            action (str ou None): acao ate a este no apartir do no pai
            cost (float): custo

        Return:
            nothing
        """
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

