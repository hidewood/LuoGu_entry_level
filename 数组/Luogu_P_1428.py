n = int(input())

nums = list(map(int, input().split()))

for i in range(n):
    total = 0
    for j in range(i):
        if nums[j] < nums[i]:
            total += 1
    print(total, end = " ")
