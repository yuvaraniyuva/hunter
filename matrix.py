n, m = map(int, input().split())

in_matrix = []
for _ in range(n):
    in_row = list(map(int, input().split()))
    in_matrix.append(in_row)

zero_rows = []
zero_cols = []

for i in range(n):
    for j in range(m):
        if in_matrix[i][j] == 0:
            zero_rows.append(i)
            zero_cols.append(j)

zero_rows = list(dict.fromkeys(zero_rows))
zero_cols = list(dict.fromkeys(zero_cols))

for r in zero_rows:
    for j in range(m):
        in_matrix[r][j] = 0

for i in range(n):
    for c in zero_cols:
        in_matrix[i][c] = 0

for row in in_matrix:
    print(*row)
