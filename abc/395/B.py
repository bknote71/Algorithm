N = int(input())

grid = [["-"] * (N + 1) for _ in range(N + 1)]

# black: #
# white: .
# nothing: -

for i in range(1, N + 1):
    j = N + 1 - i
    if i > j:
        continue

    for t1 in range(j - i + 1):
        for t2 in range(j - i + 1):
            grid[t1 + i][t2 + i] = "#" if i & 1 else "."


for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(grid[i][j], end="")
    print("\n")
