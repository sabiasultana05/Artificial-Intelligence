import math

# create node for graph
class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []


# minimax algorithm
def minimax(node, depth, maximizingPlayer):
    if depth == 0 or not node.children:
        return node.value
    if maximizingPlayer:
        maximum = -math.inf
        for child in node.children:
            child_value = minimax(child, depth - 1, False)
            maximum = max(maximum, child_value)
        return maximum
    else:
        minimum = math.inf
        for child in node.children:
            child_value = minimax(child, depth - 1, True)
            minimum = min(minimum, child_value)
        return minimum


# creating own graph
leaf1 = Node(value=1)
leaf2 = Node(value=1)
leaf3 = Node(value=2)
leaf4 = Node(value=-3)
leaf5 = Node(value=5)
leaf6 = Node(value=7)
leaf7 = Node(value=-2)
leaf8 = Node(value=-4)

node1 = Node(children=[leaf1,leaf2])
node2 = Node(children=[leaf3, leaf4])
node3 = Node(children=[leaf5, leaf6])
node4 = Node(children=[leaf7, leaf8])

node12 = Node(children=[node1, node2])
node34 = Node(children=[node3, node4])
root = Node(children=[node12, node34])


print("Maximun point that can achieve : ", end=' ')
print(minimax(root, 4, True)) # Output : maximum score is 1
