q = int(input().strip())

my_str = input().strip()

while q != 0:
    nums = input().split()
    
    if nums[0] == '1':
        my_str = my_str + nums[1]
        print(my_str)
        
    elif nums[0] == '2':
        a = int(nums[1])
        b = int(nums[2])
        
        my_str = my_str[a:a + b]
        print(my_str)
        
    elif nums[0] == '3':
        a = int(nums[1])
        my_str = my_str[:a] + nums[2] + my_str[a:]
        print(my_str)
        
    elif nums[0] == '4':
        d = my_str.find(nums[1])
        print(d)
        
    else:
        print("Error!")
        exit()    
    
    q -= 1


