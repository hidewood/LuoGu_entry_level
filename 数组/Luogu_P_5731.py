n = int(input())

nums = [[0 for _ in range(n)] for _ in range(n)]

# x y记录每次填入的位置
x = 0
y = 0
nums[0][0] = 1

# towards用来记录方向
towards = 1

count = 2
while count <= n * n:
    # 向右遍历
    while y + 1 < n and nums[x][y + 1] == 0 and towards == 1:
        y = y + 1
        nums[x][y] = count
        count += 1
    towards = 2
        
    # 向下遍历
    while x + 1 < n and nums[x + 1][y] == 0 and towards == 2:
        x = x + 1
        nums[x][y] = count
        count += 1
    towards = 3
    
    # 向左遍历
    while y - 1 >= 0 and nums[x][y - 1] == 0 and towards == 3:
        y = y - 1
        nums[x][y] = count
        count += 1    
    towards = 4
    
    # 向上遍历
    while x - 1 >= 0 and nums[x - 1][y] == 0 and towards == 4:
        x = x - 1
        nums[x][y] = count
        count += 1
    towards = 1

for i in range(n):
    for j in range(n):
        print(f"{nums[i][j]:3d}", end = "")
    print()
    
