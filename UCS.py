graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'G': 6},
        'C': {'G': 3},
         'G' :{},
        'S':{'A':2, 'B':4}
}
h2 = {'S': 7,
      'A': 5,
      'B': 5,
      'C': 3,
      'G': 0
}


def reheap_up(queue):
    index = len(queue)-1
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

        if min_child != parent:
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

def A_search(graph, start, end):
    global h2
    queue= []
    visited = []
    n = h2[start]
    path = []
    enqueue(queue, (n, start, [start]))
    while queue:
        c, node, path = dequeue(queue)
        if node == end:
            print("path is ", path)
            break
        else:
            visited.append(node)
            for p, cost in graph.items():
                if p is not visited:
                    new_cost = c + cost
                    n = h2[p]
                    c = n + new_cost
                    enqueue(queue,(c,p, path+[p]))
                    
A_search(graph, "S", "G")





