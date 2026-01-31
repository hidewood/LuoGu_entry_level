import sys

my_list = []
my_list.extend(sys.stdin.read().strip())
#print(my_list)

# 先求N
n = 0
for ele in my_list:
    if ele == '\n':
        break
    else:
        n += 1
print(n, end = " ")

# 去除my_list中的换行符
new_list = []
for ele in my_list:
    if ele != '\n':
        new_list.append(ele)

num = 1
if new_list[0] != '0':
    print("0", end = " ")
for i in range(1, len(new_list)):        
    if new_list[i] == new_list[i - 1]:
        num += 1
    else:
        print(num, end = " ")
        num = 1

print(num, end = " ")

