s = input().strip().split()

my_list = []
for line in s:
    my_list.extend(line)
    
print(len(my_list))
