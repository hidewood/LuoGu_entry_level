nums = list(map(int, input().split()))

nums.sort()

for i in range(2, nums[0] + 1):
    if nums[0] % i == 0 and nums[2] % i == 0:
        nums[0] //= i
        nums[2] //= i

print(f"{nums[0]}/{nums[2]}")
