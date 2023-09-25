# exemple case à la position 0:2 = [(0,1), 0, 1] -> [position_bulb, pas_y, pas_x]

tab = [[[(0, 0), 0, 1], [(0, 0), 0, 0]],
       [[(1, 1), 0, 0], [(1, 1), 0, -1]]]
tab_values = [[1, 0], [None, 1]]
tab_columns = [1, 2]
tab_lines = [2, 1]

def tab_to_string(tab):
    txt = '_'*(len(tab)*2+1)
    txt += '\n'
    for line in tab:
        txt += '|'
        for case in line :
            if case == 0:
                txt += '0'
            elif case == 1:
                txt += '#'
            else:
                txt += ' '
            txt += '|'
        txt += '\n'
        txt += '_'*(len(tab)*2+1) + '\n'
    return txt

def get_bulb(space_x, space_y):
    return tab[space_y][space_x][0]

def fill_with_zeros(x, y):
    #Vide une colonne ou une ligne
    if x:
        for new_y in range(len(tab_values)):
            ret_unfill = unfill_space(x, new_y)
            if not ret_unfill:
                return False
    else:
        for new_x in range(len(tab_values)):
            ret_unfill = unfill_space(new_x, y)
            if not ret_unfill:
                return False

def count_line_column(x, y):
    if x:
        values = [a[x] for a in tab_values]
        number_values = tab_columns[x]
    else:
        values = tab_values[y]
        number_values = tab_lines[y]

    count = values.count(1)

    if count > number_values:
        return False
    elif count == number_values:
        return fill_with_zeros(x, y)

def test_space(space_x, space_y):
    pass

def unfill_space(space_x, space_y):
    # Place un 0 sur l'espace et arrête de remplir le reste du thermomètre
    case = tab[space_y][space_x]
    while case[1] != 0 or case[2] != 0:


def try_fill_space(space_x, space_y):
    if tab_values[space_y][space_x] == 0 or not test_space(space_x, space_y):
        return False
    else:
        tab_values[space_y][space_x] = 1

def fill_term(bulb, pos_max_x, pos_max_y):
    #Remplis un termometre depuis son bulbe jusqu'à une position, ou retourne False si c'est impossible
    pos_x, pos_y = bulb
    ret_fill = try_fill_space(pos_x, pos_y)
    while ret_fill and pos_x != pos_max_x and pos_y != pos_max_y:
        ret_fill = try_fill_space(pos_x, pos_y)
        if ret_fill:
            pos_x, pos_y = ret_fill
        else:
            return False