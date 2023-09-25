import csv

clues = []

with open("clues.json", encoding='utf-8') as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:
        if line[2] and line[3]:
            clues.append([line[2], line[3]])


print(clues)
