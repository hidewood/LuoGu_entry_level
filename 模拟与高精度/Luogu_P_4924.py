import sys

line1 = sys.stdin.readline().split()
if not line1: exit()

n, m = map(int, line1)

num = 1
square = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        square[i][j] = num
        num += 1

def round(square, x, y, z, r):
    new_square = [row[:] for row in square]
    x0, y0 = x - r - 1, y - r - 1
    if z == 0:
        for i in range(x - r - 1, x + r):
            for j in range(y - r - 1, y + r):
                new_square[x0 + j - y0][y0 + 2 * r - i + x0] = square[i][j]

    if z == 1:
        for i in range(x - r - 1, x + r):
            for j in range(y - r - 1, y + r):
                new_square[x0 + 2 * r - j + y0][y0 + i - x0] = square[i][j]
                
    return new_square

while m != 0:
    x, y, r, z = map(int, sys.stdin.readline().split())
    square = round(square, x, y, z, r)

    m -= 1
    
for row in square:
    print(*(row))
    
