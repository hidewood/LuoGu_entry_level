import sys

# Convert n and m to integers immediately
line1 = sys.stdin.readline().split()
if not line1: exit()
n, m = map(int, line1)

# Read the grid
boom = [list(line.strip()) for line in sys.stdin.readlines()]
ans = [["" for _ in range(m)] for _ in range(n)]

# Define the 8 directions (dx, dy)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(n):
    for j in range(m):
        if boom[i][j] == '*':
            ans[i][j] = '*'
        else:
            count = 0
            # Check all 8 neighbors
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                
                # Boundary Check: ensures the neighbor is inside the grid
                if 0 <= nx < n and 0 <= ny < m:
                    if boom[nx][ny] == '*':
                        count += 1
            ans[i][j] = str(count)

# Output the result
for row in ans:
    print("".join(row))
