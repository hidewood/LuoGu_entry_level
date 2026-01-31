n = 4

dist_alph = {"A": 0, "B": 0, "C": 0,
             "D": 0, "E": 0, "F": 0,
             "G": 0, "H": 0, "I": 0,
             "J": 0, "K": 0, "L": 0,
             "M": 0, "N": 0, "O": 0,
             "P": 0, "Q": 0, "R": 0,
             "S": 0, "T": 0, "U": 0,
             "V": 0, "W": 0, "X": 0,
             "Y": 0, "Z": 0}

while n != 0:
    s = []
    s.extend(input())
    
    for i in s:
        if i >= "A" and i <= "Z":
            dist_alph[i] += 1
    # print(dist_alph)
    n -= 1

# print(dist_alph)
max_num = 0
for i in dist_alph:
    if dist_alph[i] >= max_num:
        max_num = dist_alph[i]
    
# print(max_num)
list_answer = [[" " for i in range(max_num + 1)] for j in range(26)]

# 对二维列表的每个一维元素进行处理
first_element = "A"
for i in range(26):
    list_answer[i][max_num] = first_element
    
    # dist_alph[i] 是字母出现的次数
    for j in range(max_num - 1, max_num - 1 - dist_alph[first_element], -1):
        list_answer[i][j] = "*"

    first_element = chr(ord(first_element) + 1)


# 打印结果
for i in range(max_num + 1):
    for j in range(26):
        print(list_answer[j][i], end = " ")
    
    print()
    

# [[" ", " ", ..., "A"], [], [], [], [], [], [], [], []]