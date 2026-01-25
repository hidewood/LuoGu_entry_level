import sys

n, m, k = map(int, input().split())

nums = [[0 for _ in range(n)] for _ in range(n)]

# 处理火把
for _ in range(m):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    
    # 火把本身
    nums[x][y] = 1
    
    # 处理上边
    if x - 1 >= 0: 
        nums[x - 1][y] = 1
    if x - 2 >= 0:
        nums[x - 2][y] = 1
    
    # 处理下边
    if x + 1 < n:
        nums[x + 1][y] = 1
    if x + 2 < n:
        nums[x + 2][y] = 1
   
    # 处理左边
    if y - 1 >= 0:
        nums[x][y - 1] = 1
    if y - 2 >= 0:
        nums[x][y - 2] = 1
   
    # 处理右边
    if y + 1 < n:
        nums[x][y + 1] = 1
    if y + 2 < n:
        nums[x][y + 2] = 1
   
    # 处理四周
    if x - 1 >= 0 and y - 1 >= 0:
        nums[x - 1][y - 1] = 1
    if x - 1 >= 0 and y + 1 < n:
        nums[x - 1][y + 1] = 1
    if x + 1 < n and y - 1 >= 0:
        nums[x + 1][y - 1] = 1
    if x + 1 < n and y + 1 < n:
        nums[x + 1][y + 1] = 1
    
# 处理萤石
for i in range(k):
    x, y = map(int, input().split())
    x = x - 1
    y = y - 1
    
    # 萤石本身
    nums[x][y] = 1
    
    # 处理上边
    if x - 1 >= 0: 
        nums[x - 1][y] = 1
    if x - 2 >= 0:
        nums[x - 2][y] = 1
    
    # 处理下边
    if x + 1 < n:
        nums[x + 1][y] = 1
    if x + 2 < n:
        nums[x + 2][y] = 1
   
    # 处理左边
    if y - 1 >= 0:
        nums[x][y - 1] = 1
    if y - 2 >= 0:
        nums[x][y - 2] = 1
   
    # 处理右边
    if y + 1 < n:
        nums[x][y + 1] = 1
    if y + 2 < n:
        nums[x][y + 2] = 1
   
    # 处理四周
    if x - 1 >= 0 and y - 1 >= 0:
        nums[x - 1][y - 1] = 1
    if x - 1 >= 0 and y + 1 < n:
        nums[x - 1][y + 1] = 1
    if x + 1 < n and y - 1 >= 0:
        nums[x + 1][y - 1] = 1
    if x + 1 < n and y + 1 < n:
        nums[x + 1][y + 1] = 1
        
    # 处理左上块
    if x - 2 >= 0 and y - 2 >= 0:
        nums[x - 2][y - 2] = 1
    if x - 1 >= 0 and y - 2 >= 0:
        nums[x - 1][y - 2] = 1
    if x - 2 >= 0 and y - 1 >= 0:
        nums[x - 2][y - 1] = 1
    
    # 处理右上块
    if x - 2 >= 0 and y + 2 < n:
        nums[x - 2][y + 2] = 1
    if x - 1 >= 0 and y + 2 < n:
        nums[x - 1][y + 2] = 1
    if x - 2 >= 0 and y + 1 < n:
        nums[x - 2][y + 1] = 1
    
    # 处理左下块
    if x + 2 < n and y - 2 >= 0:
        nums[x + 2][y - 2] = 1
    if x + 1 < n and y - 2 >= 0:
        nums[x + 1][y - 2] = 1
    if x + 2 < n and y - 1 >= 0:
        nums[x + 2][y - 1] = 1
    
    # 处理右下块
    if x + 2 < n and y + 2 < n:
        nums[x + 2][y + 2] = 1
    if x + 1 < n and y + 2 < n:
        nums[x + 1][y + 2] = 1
    if x + 2 < n and y + 1 < n:
        nums[x + 2][y + 1] = 1
        
total = 0
for i in range(n):
    for j in range(n):
        if nums[i][j] == 0:
            total += 1

print(total)