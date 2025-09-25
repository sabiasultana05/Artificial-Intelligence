graph = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW'],
        'T': ['']
    }

colors = ['Red', 'Green', 'Blue']


def is_safe(vertex, color, color_assignment, graph):
    for neighbor in graph[vertex]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

def solve(vertex, color_assignment, graph, colors):
    if vertex not in color_assignment:
        for color in colors:
            if is_safe(vertex, color, color_assignment, graph):
                color_assignment[vertex] = color
                remaining_vertices = []
                for v in graph.keys():
                    if v not in color_assignment:
                        remaining_vertices.append(v)

                if not remaining_vertices:
                    return color_assignment
                else:
                    next_vertex = remaining_vertices[0]
                    result = solve(next_vertex, color_assignment, graph, colors)
                    if result is not None:
                        return result
                color_assignment.pop(vertex)
        return None
    else:
        remaining_vertices = []
        for v in graph.keys():
            if v not in color_assignment:
                remaining_vertices.append(v)

        if not remaining_vertices:
            return color_assignment
        else:
            next_vertex = remaining_vertices[0]
            return solve(next_vertex, color_assignment, graph, colors)


solution = solve('WA', {}, graph, colors)
if solution is not None:
    print("Solution found:")
    for state, color in solution.items():
        print(f"{state}: {color}")
else:
    print("No solution exists!")
