import itertools, enchant

word = "belusconi"
d = enchant.Dict("en_US")
for word in ["".join(perm) for perm in itertools.permutations(word)]:
    if d.check(word):
        print(word)