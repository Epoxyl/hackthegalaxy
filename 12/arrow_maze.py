# d : (1, 0), t : (-1, 0), l : (0, -1), r : (0, 1) , dr : (1, 1), dl : (1, -1) , tr : (-1, 1) , tl : (-1, -1)
from copy import copy, deepcopy

original_maze = [
    [[1, (1, 1)], [0, (1, 0)], [0, (1, 0)], [0, (1, 1)], [0, (0, -1)], [0, (0, -1)], [0, (1, 0)], [0, (1, -1)]],
    [[0, (-1, 1)], [0, (1, 0)], [16, (0, 1)], [17, (1, 1)], [52, (1, 0)], [0, (1, 0)], [0, (1, 0)], [0, (0, -1)]],
    [[44, (0, 1)], [43, (0, -1)], [0, (-1, 0)], [14, (1, 1)], [0, (1, -1)], [0, (-1, 1)], [10, (1, 0)], [45, (0, -1)]],
    [[0, (1, 0)], [27, (0, 1)], [0, (-1, 1)], [0, (-1, -1)], [15, (-1, -1)], [28, (0, 1)], [0, (1, 0)], [0, (0, -1)]],
    [[60, (0, 1)], [59, (0, -1)], [26, (-1, -1)], [62, (0, 1)], [63, (1, 1)], [58, (0, -1)], [0, (1, 0)], [61, (0, -1)]],
    [[0, (1, 0)], [0, (0, 1)], [55, (1, 0)], [54, (0, -1)], [0, (1, 1)], [0, (0, 1)], [13, (-1, -1)], [0, (1, 0)]],
    [[0, (-1, -1)], [0, (1, 1)], [56, (0, 1)], [57, (-1, 1)], [53, (-1, -1)], [0, (0, -1)], [0, (-1, 0)], [0, (-1, 0)]],
    [[0, (0, 1)], [0, (-1, -1)], [0, (-1, 0)], [33, (0, -1)], [0, (0, 1)], [0, (-1, 0)], [0, (0, -1)], [64, ""]]
]

def get_found_numbers(maze):
    found = []
    for line in maze:
        for case in line:
            if case[0]:
                found.append(case[0])

    return sorted(found)


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

def resolve(maze, line, column, number, next_number_to_found):
    if number == next_number_to_found and maze[line][column][0] != number:
        # Si c'est un nombre qu'on est sensé trouver mais que la valeur de la case est différente, on return false

        return -1


    if maze[line][column][0] == next_number_to_found:
        # Si la valeur de la case est bien la prochaine à trouver on change la prochaine valeur
        if number >= 45:
            print("{} found ! ".format(number))
            print(maze_to_string(maze))
        if next_number_to_found == 64:
            raise Exception("found")
        next_number_to_found = get_next_found_number(number)

    else:
        # Sinon on place le numéro en cours sur la case
        maze[line][column][0] = number

    arrow_y, arrow_x = maze[line][column][1] # arrow_y et arrow_x correspondent à la direction x et y
    x = column + arrow_x
    y = line + arrow_y
    ret = False
    while x >= 0 and x <= 7 and y >= 0 and y <= 7 and (not ret or ret == -1):
        # Tant que la case est dans le tableau et que le bon chemin n'est pas trouvé

        next_case = maze[y][x]                              # La case à tester
        next_number = next_case[0]
        if not next_number or next_number == number + 1:
            # Si la valeur de la prochaine case = 0 ou = au prochain numéro

            maze_copy = deepcopy(maze)                      # permet d'avoir une copie du tableau qui ne sera pas modifiée

            ret = resolve(maze_copy, y, x, number + 1, next_number_to_found)
        x += arrow_x
        y += arrow_y

    return False

found_numbers = get_found_numbers(original_maze)
print(found_numbers)
print(maze_to_string(original_maze))
resolve(original_maze, 0, 0, 1, 1)