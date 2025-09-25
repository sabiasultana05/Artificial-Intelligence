# Define graph in a dictionary
# Keys represet nodes name and corresponding values reprsent it's neighbours

graph = { 0 : [1 ,2],
          1 : [],
          2 : [0,3],
          3 : [3]
}

# Function for breath first search
def bfs(source):
    global graph
    queue = []
    visited = []

    if source not in graph:
        print("source not found")
        return


    queue.append(source)

    while len(queue) > 0:
        x = queue.pop(0)
        print(x)

        if x not in visited:
           visited.append(x)
           for i in graph[x]:
               if i not in visited:
                   queue.append(i)

# run the code with 2nd node

bfs(2) # uput path : 2 0 3 1