# d : (1, 0), t : (-1, 0), l : (0, -1), r : (0, 1) , dr : (1, 1), dl : (1, -1) , tr : (-1, 1) , tl : (-1, -1)
from copy import copy, deepcopy

original_maze = [
    [[1, (1, 1)], [0, (1, 0)], [0, (1, 0)], [0, (1, 1)], [0, (0, -1)], [0, (0, -1)], [0, (1, 0)], [0, (1, -1)]],
    [[0, (-1, 1)], [0, (1, 0)], [0, (0, 1)], [17, (1, 1)], [52, (1, 0)], [0, (1, 0)], [0, (1, 0)], [0, (0, -1)]],
    [[0, (0, 1)], [43, (0, -1)], [0, (-1, 0)], [14, (1, 1)], [0, (1, -1)], [0, (-1, 1)], [10, (1, 0)], [45, (0, -1)]],
    [[0, (1, 0)], [0, (0, 1)], [0, (-1, 1)], [0, (-1, -1)], [15, (-1, -1)], [28, (0, 1)], [0, (1, 0)], [0, (0, -1)]],
    [[60, (0, 1)], [59, (0, -1)], [26, (-1, -1)], [0, (0, 1)], [0, (1, 1)], [0, (0, -1)], [0, (1, 0)], [61, (0, -1)]],
    [[0, (1, 0)], [0, (0, 1)], [55, (1, 0)], [54, (0, -1)], [0, (1, 1)], [0, (0, 1)], [0, (-1, -1)], [0, (1, 0)]],
    [[0, (-1, -1)], [0, (1, 1)], [56, (0, 1)], [0, (-1, 1)], [53, (-1, -1)], [0, (0, -1)], [0, (-1, 0)], [0, (-1, 0)]],
    [[0, (0, 1)], [0, (-1, -1)], [0, (-1, 0)], [33, (0, -1)], [0, (0, 1)], [0, (-1, 0)], [0, (0, -1)], [64, ""]]
]

def get_found_numbers(maze):
    found = []
    for line in maze:
        for case in line:
            if case[0]:
                found.append(case[0])

    return sorted(found, reverse=True)


def get_next_found_number(number):
    index = found_numbers.index(number)
    return found_numbers[index + 1]

def maze_to_string(maze):
    maze_str = "_________________________________________\n"
    for line in maze:
        line_str = "|"
        for case in line:
            line_str += " {} |".format(str(case[0]).rjust(2, '0'))
        maze_str += line_str + "\n"
    maze_str += "_________________________________________\n"
    return maze_str

def get_line(maze, line, column):
    return maze[line]

def get_column(maze, line, column):
    return [maze[line_maze][column] for line_maze in range(0,8)]

def get_diag_1(maze, line, column):
    while
    return [maze[y][x] for (y,x) in []]

def resolve(maze, line, column, number, next_number_to_found):
    if maze[line][column][0] and maze[line][column][0] != next_number_to_found:
        return False

    if maze[line][column][0] == next_number_to_found:
        next_number_to_found = get_next_found_number(number)
    tests = [(0, 1), (1, 0), (1,1)]


    ret = False
    # par ligne
    x = column
    y = line
    while x >= 0:
        if maze[y][x][1] == "r":
            ret = resolve(deepcopy(maze), y, x, number-1, next_number_to_found)
        x -= 1
    x = column
    while x <= 7:
        if maze[y][x][1] == "l":
            ret = resolve(deepcopy(maze), y, x, number-1, next_number_to_found)
        x += 1
    # par colonne
    while y >= 0:
        if maze[y][x][1] == "":
            ret = resolve(deepcopy(maze), y, x, number-1, next_number_to_found)
        y -= 1
    while y <= 7:
        if maze[y][x][1] == "r":
            ret = resolve(deepcopy(maze), y, x, number-1, next_number_to_found)
        y += 1
    # par diag 1

    # par diag 2

    return ret

found_numbers = get_found_numbers(original_maze)
print(found_numbers)
print(maze_to_string(original_maze))
resolve(original_maze, 7, 7, 64, 64)