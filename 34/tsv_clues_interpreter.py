import csv
import json
import sys

maxInt = sys.maxsize
while True:
    # decrease the maxInt value by factor 10
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt / 10)

clues = { }
only_clues = []
with open("../clues.tsv", encoding='utf-8') as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:
        if not line[2] or not line[3]:
            continue
        if line[2] == 'RTE':
            print(line)
        only_clues.append(line[3])
        if line[2].lower() in clues.keys():
            clues[line[2].lower()].append(line[3].lower())
        else:
            clues[line[2].lower()] = [line[3].lower()]

open('clues.json', 'w').close()

with open('clues.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(clues))

open('only_clues.json', 'w').close()

with open('only_ clues.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(clues))
