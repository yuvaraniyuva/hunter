a, k = map(int, input().split())
nums = list(map(int, input().split()))

if k in nums:
    print('YES')
else:
    for i in range(a):
        s = 0
        for j in range(i, a):
            s += nums[j]
            if s > k:
                break
            elif s == k:
                print('YES')
                quit(0)
    print('NO')
