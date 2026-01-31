i = int(input())

nums = []
for j in range(i):
    nums.append(input().split())
    
# print(nums)
# col用来记录上一次的算术类型
col = 'a'
for j in range(i):
    if nums[j][0] == 'a':
        print(f"{nums[j][1]}+{nums[j][2]}={int(nums[j][1])+int(nums[j][2])}")
        print(len(f"{nums[j][1]}+{nums[j][2]}={int(nums[j][1])+int(nums[j][2])}"))
        col = 'a'
    
    elif nums[j][0] == 'b':
        print(f"{nums[j][1]}-{nums[j][2]}={int(nums[j][1])-int(nums[j][2])}")
        print(len(f"{nums[j][1]}-{nums[j][2]}={int(nums[j][1])-int(nums[j][2])}"))
        col = 'b'
        
    elif nums[j][0] == 'c':
        print(f"{nums[j][1]}*{nums[j][2]}={int(nums[j][1])*int(nums[j][2])}")
        print(len(f"{nums[j][1]}*{nums[j][2]}={int(nums[j][1])*int(nums[j][2])}"))
        col = 'c'
    else:
        if col == 'a':
            print(f"{nums[j][0]}+{nums[j][1]}={int(nums[j][0])+int(nums[j][1])}")
            print(len(f"{nums[j][0]}+{nums[j][1]}={int(nums[j][0])+int(nums[j][1])}"))
        
        elif col == 'b':
            print(f"{nums[j][0]}-{nums[j][1]}={int(nums[j][0])-int(nums[j][1])}")
            print(len(f"{nums[j][0]}-{nums[j][1]}={int(nums[j][0])-int(nums[j][1])}"))
            
        elif col == 'c':
            print(f"{nums[j][0]}*{nums[j][1]}={int(nums[j][0])*int(nums[j][1])}")
            print(len(f"{nums[j][0]}*{nums[j][1]}={int(nums[j][0])*int(nums[j][1])}"))
        