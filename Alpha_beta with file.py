import math

class Node:
    def __init__(self, name, value, children):
        self.name = name
        self.value = value
        self.children = children

# give graph infrmation in a text file
def read_file():
    nodes = {}
    with open("alpha_beta_input.txt", 'r') as file:
        non_term = file.readline()
        info = non_term.strip().split()
        n = int(info[0])
        root = info[1]
        for i in range(0, n):
            info = file.readline()
            item = info.strip().split(' ')
            name = item[0].strip()
            children = []
            children = item[1:]
            value = None
            nodes[name] = Node(name, value, children)

        t = int(file.readline())

        for i in range(0, t):
            info = file.readline()
            item = info.strip().split(' ')
            name = item[0].strip()
            value = float(item[1].strip())
            children = None
            nodes[name] = Node(name, value, children)
    return root, nodes

track = []
pruned = []
def alpha_beta(node, depth, alpha, beta, maximizing_player, path):
    track.append(node.name)
    if node.children is None or depth == 0:
        return node.value, path + [node.name]

    if maximizing_player:
        value = -math.inf
        best_path = []
        for child in node.children:
            child_node = nodes[child]
            child_value, child_path = alpha_beta(child_node, depth - 1, alpha, beta, False, path + [node.name])
            if child_value > value:
                value = child_value
                best_path = child_path

            if beta <= child_value:
                for i in node.children:
                    if i not in track:
                        pruned.append(i)
                        if nodes[i].children is not None:
                            for x in nodes[i].children:
                                pruned.append(x)
                break

            alpha = max(alpha, value)
        return value, best_path


    else:
        value = math.inf
        best_path = []
        for child in node.children:
            child_node = nodes[child]
            child_value, child_path = alpha_beta(child_node, depth - 1, alpha, beta, True, path + [node.name])
            if child_value < value:
                value = child_value
                best_path = child_path
            if child_value <= alpha:
                for i in node.children:
                    if i not in track:
                        pruned.append(i)
                        if nodes[i].children is not None:
                            for x in nodes[i].children:
                                pruned.append(x)
                break
            beta = min(beta, child_value)

        return value, best_path


root, nodes = read_file()

root_node = nodes[root]
result, path = alpha_beta(root_node, 4, -math.inf, math.inf, True, [])
print("Optimal value:", result)
print("Path", end=' : ')
for i in path:
    print(i, end=' ')
print('\n')


print("Pruned Nodes are :", end=' ')
for i in pruned:
    print(i, end=' ')