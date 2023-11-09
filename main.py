#!/usr/bin/python3
""" Entry point """


if __name__ == '__main__':
    from uniform_cost_search import uniform_cost_search
    graph = {
        'A': [('B', 5), ('D', 2)],
        'B': [('A', 5), ('C', 3), ('E', 4)],
        'C': [('B', 3), ('F', 7)],
        'D': [('A', 2), ('E', 6)],
        'E': [('B', 4), ('D', 6), ('F', 1)],
        'F': [('C', 7), ('E', 1)]
    }

    start_node = 'A'
    goal_node = 'F'

    caminho_minimo = uniform_cost_search(graph, start_node, goal_node)

    print(
            f'Caminho de {start_node} para {goal_node}: {caminho_minimo}'
            if caminho_minimo
            else f'Não há caminho de {start_node} para {goal_node}'
        )
