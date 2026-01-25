n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]

# x y 用来记录数字填充的位置
x = 0
y = n // 2

for i in range(1, n * n + 1):
    grid[x][y] = i
    if ((x == 0 and y != n - 1)):
        x = n - 1
        y += 1
    elif (y == n - 1 and x != 0):
        y = 0
        x -= 1
    elif (x == 0 and y == n - 1):
        x += 1
    elif (x != 0 and y != n - 1):
        if grid[x - 1][y + 1] == 0:
            x = x - 1
            y = y + 1
        else:
            x = x + 1
            
for i in range(n):
    for j in range(n):
        print(grid[i][j], end = " ")
    print()

