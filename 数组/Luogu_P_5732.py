n = int(input())

nums = [[0 for _ in range(n)] for _ in range(n)]

# 填第一列数字
for i in range(n):
    nums[i][0] = 1

# 填中间列数字
for i in range(1, n):
    for j in range(1, n - 1):
        nums[i][j] = nums[i - 1][j - 1] + nums[i - 1][j]

# 填最后一列数字
for i in range(n):
    nums[i][i] = 1

for i in range(n):
    for j in range(n):
        if nums[i][j] != 0:
            print(nums[i][j], end = " ")
    print()

       