nums = list(map(int, input().split()))

n = nums[0]
length = len(nums) - 1

# 记录当前是填0还是1
cur = 0

# 记录当前行已经填的数字个数
total = 0
for i in range(1, length + 1):
    if cur == 0:
        for j in range(nums[i]):
            if total == n:
                print()
                total = 0
            print(0, end = "")
            total += 1
        cur = 1
        continue

    if cur == 1:
        for j in range(nums[i]):
            if total == n:
                print()
                total = 0
            print(1, end = "")
            total += 1
        cur = 0

