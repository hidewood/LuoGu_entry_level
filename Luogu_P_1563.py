# 思路是先用二维列表存储每个小人的信息，然后进行循环判断，注意取余
import sys

line1 = sys.stdin.readline().split()
if not line1: exit()

n, m = map(int, line1)

people = []
for _ in range(n):
    people.append(sys.stdin.readline().split())
    
# print(people)
command = []
for _ in range(m):
    command.append(sys.stdin.readline().split())
    
# print(command)

pos = 0
for row in command:
    if int(people[pos][0]) != int(row[0]):
        pos = (pos + int(row[1])) % n
    else:
        pos = (pos - int(row[1])) % n

print(people[pos][1])
