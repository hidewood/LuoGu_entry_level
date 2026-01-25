nums = list(map(int, input().split()))
str = input()

nums.sort()
print(str)

if str == "ABC":
    print(f"{nums[0]} {nums[1]} {nums[2]}", end="")
elif str == "ACB":
    print(f"{nums[0]} {nums[2]} {nums[1]}", end="")
elif str == "BAC":
    print(f"{nums[1]} {nums[0]} {nums[2]}", end="")
elif str == "BCA":
    print(f"{nums[1]} {nums[2]} {nums[0]}", end="")
elif str == "CAB":
    print(f"{nums[2]} {nums[0]} {nums[1]}", end="")
elif str == "CBA":
    print(f"{nums[2]} {nums[1]} {nums[0]}", end="")
    
