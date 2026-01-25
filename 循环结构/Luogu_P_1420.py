n = int(input())

nums = list(map(int, input().split()))

max_cons = 1
this_cons = 1
for i in range(1, n):
    if nums[i - 1] + 1 == nums[i]:
        this_cons += 1
        if this_cons >= max_cons:
            max_cons = this_cons
    else:
        this_cons = 1
        
print(max_cons)