n = int(input())

nums = list(map(int, input().split()))

total = 0
for i in range(n):
    found = False
    for j in range(n):
        for k in range(j + 1, n):
            if nums[j] != nums[k] and nums[i] == nums[j] + nums[k]:
                total += 1
                found = True
                break
        if found:
            break
        
print(total)