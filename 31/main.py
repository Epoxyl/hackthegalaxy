import enchant


def remove_letter(word):
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if d.check(new_word):
            print(new_word)

def invert_and_change_letter(word):
    new_word = word[::-1]
    suggestions = d.suggest(new_word)
    if suggestions:
        print(suggestions)

currencies = ["ariary", "baht", "dalasi", "dirham", "dollar", "escudo", "metical", "pound", "ringgit", "rupiah", "somoni", "togrog", "zloty"]
#with open("capitals.txt", encoding='utf-8') as f:
#    result = ""
#    for line in f.readlines():
#        result += line.lower()
#
#open('capitals.txt').close()
#
#with open("capitals.txt", 'w', encoding='utf-8') as f:
#    f.write(result)

d = enchant.request_pwl_dict('capitals.txt')
print(d.check("Paris"))

for word in currencies:
    invert_and_change_letter(word)
