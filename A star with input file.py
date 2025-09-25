#heurostic

h = {'S': 7,
      'A': 5,
      'B': 5,
      'C': 3,
      'G': 0
}


def read_graph():
    graph = {}
    file = open("A star input graph.txt", 'r')
    for line in file:
        parts = line.strip().split(':')
        node = parts[0].strip()
        neighbors = {}
        if len(parts) > 1:
            for item in parts[1].strip().split():
                neighbor, cost = item.split('_')
                neighbors[neighbor] = int(cost)
        graph[node] = neighbors

    return graph


def reheap_up(queue):
    index = len(queue) - 1
    while index > 0:
        parent_index = (index - 1) // 2
        if queue[index][0] < queue[parent_index][0]:
            queue[index], queue[parent_index] = queue[parent_index], queue[index]
            index = parent_index
        else:
            break


def reheap_down(queue):
    n = len(queue)
    parent = 0
    while True:
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2
        min_child = parent

        if left_child < n and queue[left_child][0] < queue[min_child][0]:
            min_child = left_child
        if right_child < n and queue[right_child][0] < queue[min_child][0]:
            min_child = right_child

        if min_child > parent:
            queue[parent], queue[min_child] = queue[min_child], queue[parent]
            parent = min_child
        else:
            break


def enqueue(queue, i):
    queue.append(i)
    reheap_up(queue)


def dequeue(queue):
    x = queue.pop(0)
    reheap_down(queue)
    return x


def A_star(start, goal):
    global h
    graph = read_graph()
    visited = []
    flag = False
    n = h[start]
    queue = [(n, 0, start, [start])]

    while queue:
        sa, cost, node, path = dequeue(queue)

        if node in visited:
            continue

        visited.append(node)

        if node == goal:
            flag = True
            break

        for i, i_cost in graph[node].items():
            if i not in visited:
                n = h[i]
                new_cost = cost + i_cost
                new_path = path + [i]
                enqueue(queue, (new_cost + n, new_cost, i, new_path))

    if flag == True:
        print("path is", path)
        print("path cost is ", cost)
        # print("path cost is", cost)


A_star("S", "G")
