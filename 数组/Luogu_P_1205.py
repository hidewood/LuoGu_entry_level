import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()
    
n = int(input_data[0])
graph_list = []
for i in range(1, n + 1):
        graph_list.append(input_data[i])
# print(*graph_list)

target_list = []
for i in range(n + 1, 2 * n + 1):
    target_list.append(input_data[i])
# print(*target_list)

# 方式1
new_list_1 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_list_1[j][n - i - 1] = graph_list[i][j]
# print(*new_list_1)

# 方式2
new_list_2 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_list_2[j][n - i - 1] = new_list_1[i][j]
# print(*new_list_2)

# 方式3
new_list_3 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_list_3[j][n - i - 1] = new_list_2[i][j]
# print(*new_list_3)

# 方式4
new_list_4 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    new_list_4[i] = graph_list[i][::-1]
# print(*new_list_4)

# 方式5
new_list_5 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    new_list_5[i] = graph_list[i][::-1]

new_list_5_1 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_list_5_1[j][n - i - 1] = new_list_5[i][j]

new_list_5_2 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_list_5_2[j][n - i - 1] = new_list_5_1[i][j]

new_list_5_3 = [['0' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_list_5_3[j][n - i - 1] = new_list_5_2[i][j]

graph_list_final = []
for line in graph_list:
    # 注意：这里用 append，将拆分后的整个列表作为一个元素加入
    graph_list_final.append(list(line))

target_list_final = []
for line in target_list:
    target_list_final.append(list(line))

# 此时打印结果就是你要的二维形式：
# [['@', '-', '@'], ['-', '-', '-'], ['@', '@', '-']]


# 开始判断
if target_list_final == new_list_1:
    print(1)
    exit()
elif target_list_final == new_list_2:
    print(2)
    exit()
elif target_list_final == new_list_3:
    print(3)
    exit()
elif target_list_final == new_list_4:
    print(4)
    exit()
elif target_list_final == target_list_final or target_list_final == new_list_5_2 or target_list_final == new_list_5_3:
    print(5)
    exit()
elif target_list_final == graph_list_final:
    print(6)
    exit()
else:
    print(7)
