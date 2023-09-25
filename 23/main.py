words = [
    [12, 7, 3, 17],
    [13, 2, 14, 1, 5],
    [15, 12, 9, 3, 4],
    [11, 6, 2],
    [7, 8, 10, 16, 17],
    [4, 9, 4, 7, 16, 10, 1],
    [12, 13, 8, 11, 4, 5, 6],
    [14, 4, 6],
    [4, 7, 12, 1, 7, 2, 15],
    [16, 17, 8, 1, 4, 5],
]

chips = {
    1: 'S',
    2: 'OL',
    3: 'U',
    4: 'T',
    5: 'ION',
    6: "IST",
    7: 'H',
    8: 'E',
    9: 'WO',
    10: 'RD',
    11: 'P',
    12: 'RE',
    13: 'C',
    14: 'LU',
    15: 'D',
    16: 'I', #ok
    17: 'NG', #ok
}


def tostring():
    print("here")
    i = 1
    for word in words:
        word_str = ""
        for chip in word:
            if chip in chips.keys():
                word_str += chips[chip]
            else:
                word_str += '[{}]'.format(chip)
        print("{} : {}".format(i, word_str))
        i += 1


tostring()
