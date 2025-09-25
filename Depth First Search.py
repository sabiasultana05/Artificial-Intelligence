# Define graph in a dictionary
# Keys represet nodes name and corresponding values reprsent it's neighbours

graph = {0:[1, 3],
         1:[0,2,3,5,6],
         2:[1,3,4,5],
         3:[0,1,2,4],
         4:[2,3,6],
         5:[1,2],
         6:[1,4]
}


# Function for depth first search
def dfs(source):
    global graph
    stack = []
    visited = []

    if source not in graph:
        print("source not found")
        return

    stack.append(source)

    while len(stack)>0:
        x = stack.pop()

        if x not in visited:
            visited.append(x)
            print(x)
            for i in graph[x]:
                if i not in visited:
                    stack.append(i)

# run the code with 0th node

dfs(0) # output path : 0 3 4 6 1 5 2