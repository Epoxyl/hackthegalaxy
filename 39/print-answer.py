def print_answer(answers, word):
    if not len(answers):
        print(word)
        return

    case = answers[0].strip()
    if '|' in case:
        possibilities = case.split('|')
        for possibility in possibilities:
            print_answer(answers[1:], word+possibility)
    else:
        print_answer(answers[1:], word+case)
    return

with open("anwer") as f:
    lines = f.readlines()

print_answer(lines, '')

