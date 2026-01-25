nums = list(map(int, input().split()))

n = len(nums)

for i in range(n - 2, -1, -1):
    print(nums[i], end = " ")
    