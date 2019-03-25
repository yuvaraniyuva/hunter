n = int(input())
nums = list(map(int, input().split()))

result = []
j = 0
for i in range(n):
    result.append(1)
    for j in range(n):
        if i != j:
            result[i] *= nums[j]

print(*result)
