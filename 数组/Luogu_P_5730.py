n = int(input())
str_num = input().strip()

my_list = [[] for _ in range(10)]

my_list[0] = ["XXX", "X.X", "X.X", "X.X", "XXX"]
my_list[1] = ["..X", "..X", "..X", "..X", "..X"]
my_list[2] = ["XXX", "..X", "XXX", "X..", "XXX"]
my_list[3] = ["XXX", "..X", "XXX", "..X", "XXX"]
my_list[4] = ["X.X", "X.X", "XXX", "..X", "..X"]
my_list[5] = ["XXX", "X..", "XXX", "..X", "XXX"]
my_list[6] = ["XXX", "X..", "XXX", "X.X", "XXX"]
my_list[7] = ["XXX", "..X", "..X", "..X", "..X"]
my_list[8] = ["XXX", "X.X", "XXX", "X.X", "XXX"]
my_list[9] = ["XXX", "X.X", "XXX", "..X", "XXX"]

input_list = []
for c in str_num:
    input_list.append(int(c))

# 比如打印012，先按照my_list[0][0] my_list[1][0] my_list[2][0]

idx = 0
for i in range(5):
    for j in input_list:
        idx += 1
        print(my_list[j][i], end = "")
        if idx != len(input_list):
            print('.', end = "")
        else:
            idx = 0
    print()
