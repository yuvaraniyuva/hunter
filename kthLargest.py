n, k = map(int, input().split())

nums = list(map(int, input().split()))

for i in range(k):
    for j in range(i, n):
        if nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print(nums[k-1])
