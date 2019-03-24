from itertools import permutations

str = input()

out_list = permutations(str)
out_list = list(dict.fromkeys(out_list))

for perm in out_list:
    print(''.join(perm))
