def graph_coloring(graph, colors):
    coloring = {}
    for node in graph:
        available_colors = set(colors)
        for neighbor in graph[node]:
            if neighbor in coloring:
                available_colors.discard(coloring[neighbor])
        if available_colors:
            selected_color = min(available_colors)
            coloring[node] = selected_color
        else:
            raise Exception("No valid color found for node {}".format(node))
    return coloring

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

result = graph_coloring(graph, colors)
print(result)
