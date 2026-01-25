n = int(input())

nums = list(map(int, input().split()))

nums.sort()

total = 0
for i in range(1, n - 1):
    total += nums[i]
    
print(f"{total/(n - 2):.2f}")