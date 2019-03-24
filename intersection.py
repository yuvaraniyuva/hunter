n, k = map(int, input().split())

input_sets = []

for _ in range(n):
    in_set = set(map(int, input().split()))
    input_sets.append(in_set)

output_list = set.intersection(*input_sets)

print(*output_list)
