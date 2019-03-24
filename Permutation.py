from itertools import permutations

str = input()

outlist = permutations(str)
outlist = list(dict.fromkeys(outlist))

for perm in outlist:
    print(''.join(perm))
