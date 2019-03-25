n, m = map(int, input().split())

matrix = []
for _ in range(n):
    in_row = list(map(int, input().split()))
    matrix.append(in_row)

zero_rows = []
zero_cols = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero_rows.append(i)
            zero_cols.append(j)

zero_rows = list(dict.fromkeys(zero_rows))
zero_cols = list(dict.fromkeys(zero_cols))

for r in zero_rows:
    for j in range(m):
        matrix[r][j] = 0

for i in range(n):
    for c in zero_cols:
        matrix[i][c] = 0

for row in matrix:
    print(*row)
