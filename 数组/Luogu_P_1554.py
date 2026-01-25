m, n = map(int, input().split())

nums = [0 for _ in range(10)]

for i in range(m, n + 1):
    d = i
    while d != 0:
        nums[d % 10] += 1
        d //= 10
    
for i in nums:
    print(i, end = " ")
    
