l, m = map(int, input().split())

tree_list = []
for i in range(0, l + 1):
    tree_list.append(1)

while m != 0:
    u, v = map(int, input().split())
    
    for i in range(u, v + 1):
        tree_list[i] = 0
    m -= 1

total = 0

for i in range(0, l + 1):
    if tree_list[i] == 1:
        total += 1

print(total)