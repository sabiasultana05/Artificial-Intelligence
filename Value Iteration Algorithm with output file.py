height = 3
width = 4
grid_world = {(1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0,
              (2, 1): 0, (2, 2): 'None', (2, 3): 0, (2, 4): 0,
              (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0
              }
policy = {}


def rewards(a, b):
    if (a, b) == (1, 4):
        return +1.00
    elif (a, b) == (2, 4):
        return -1.00
    else:
        return 0


def is_terminal(a, b):
    if (a, b) == (1, 4) or (a, b) == (2, 4):
        return True
    else:
        return False


def is_blocked(a, b):
    if (a, b) == (2, 2):
        return True
    else:
        return False


def get_neighbors(a, b):
    global grid_world, height, width
    neighbors = {}

    if is_blocked(a, b):
        return

    if b >= 1:
        if not is_terminal(a, b):
            if b == 1:
                neighbors['left'] = (a, b)

            else:
                if is_blocked(a, b - 1):
                    neighbors['left'] = (a, b)
                else:
                    neighbors['left'] = (a, b - 1)

    if b <= width:
        if not is_terminal(a, b):
            if b == width:
                neighbors['right'] = (a, b)
            else:
                if is_blocked(a, b + 1):
                    neighbors['right'] = (a, b)
                else:
                    neighbors['right'] = (a, b + 1)
        else:
            neighbors['right'] = 'exit'

    if a >= 1:
        if not is_terminal(a, b):
            if a == 1:
                neighbors['up'] = (a, b)
            else:
                if is_blocked(a - 1, b):
                    neighbors['up'] = (a, b)
                else:
                    neighbors['up'] = (a - 1, b)

    if a <= height:
        if not is_terminal(a, b):
            if a == height:
                neighbors['down'] = (a, b)
            else:
                if is_blocked(a + 1, b):
                    neighbors['down'] = (a, b)
                else:
                    neighbors['down'] = (a + 1, b)

    return neighbors


def print_grid():
    global grid_world, height, width
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            value = grid_world[(i, j)]
            if value != 'None':
                grid_world[(i, j)] = format(value, '.2f')
                print(grid_world[(i, j)], end='   ')
            else:
                grid_world[(i, j)] = value
                print(grid_world[(i, j)], end='   ')

        print('\n')


def print_policy():
    print('\n\n')
    global grid_world, height, width, policy
    for i in range(1, height + 1):
        for j in range(1, width + 1):
            print(policy[(i, j)], end='   ')
        print('\n')


# to write output in a text file - optional

def print_grid_file(filename):
    global grid_world, height, width, policy
    with open(filename, 'w') as file:
        file.write('\nOptimal Values:')
        file.write('\n\n')
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                n = grid_world[(i, j)]
                file.write(n)
                file.write("\t\t")

            file.write('\n\n\n')

        file.write('\nOptimal Policy')
        file.write('\n\n')
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                n = policy[(i, j)]
                file.write(n)
                file.write("\t\t")

            file.write('\n\n\n')


def value_iteration():
    global grid_world, height, width, policy
    noise = 0.2
    gamma = 0.9
    old_grid = {}
    action = ['up', 'down', 'right', 'left']
    while True:
        old_grid = grid_world.copy()
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                value = grid_world[(i, j)]
                reward = rewards(i, j)

                if is_blocked(i, j):
                    grid_world[(i, j)] = old_grid[(i, j)]
                    policy[(i, j)] = "-----"

                if is_terminal(i, j):
                    max_value = reward
                    grid_world[(i, j)] = max_value
                    policy[(i, j)] = 'right'

                else:
                    neighbours = get_neighbors(i, j)
                    if neighbours is None:
                        continue
                    for move in action:
                        if move == 'left':
                            goal = neighbours['left']
                            noise1 = neighbours['up']
                            noise2 = neighbours['down']
                            max_value = ((1 - noise) * gamma * old_grid[goal]) + (
                                        (noise / 2) * gamma * old_grid[noise1]) + (
                                                (noise / 2) * gamma * old_grid[noise2])
                            if max_value > value:
                                grid_world[(i, j)] = max_value
                                policy[(i, j)] = 'left '

                        if move == 'right':
                            goal = neighbours['right']
                            noise1 = neighbours['up']
                            noise2 = neighbours['down']
                            max_value = ((1 - noise) * gamma * old_grid[goal]) + (
                                        (noise / 2) * gamma * old_grid[noise1]) + (
                                                (noise / 2) * gamma * old_grid[noise2])
                            if max_value > value:
                                grid_world[(i, j)] = max_value
                                policy[(i, j)] = 'right'

                        if move == 'up':
                            goal = neighbours['up']
                            noise1 = neighbours['left']
                            noise2 = neighbours['right']
                            max_value = ((1 - noise) * gamma * old_grid[goal]) + (
                                        (noise / 2) * gamma * old_grid[noise1]) + (
                                                (noise / 2) * gamma * old_grid[noise2])
                            if max_value > value:
                                grid_world[(i, j)] = max_value
                                policy[(i, j)] = ' up  '

                        if move == 'up':
                            goal = neighbours['down']
                            noise1 = neighbours['left']
                            noise2 = neighbours['right']
                            max_value = ((1-noise) * gamma * old_grid[goal]) + ((noise/2) * gamma * old_grid[noise1]) + (
                                    (noise/2) * gamma * old_grid[noise2])
                            if max_value > value:
                                grid_world[(i, j)] = max_value
                                policy[(i, j)] = 'down '

        if old_grid == grid_world:
            break


value_iteration()
print_grid()
print_policy()
print_grid_file('Value_iteration_output.txt')
