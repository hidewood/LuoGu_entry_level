import sys

n = int(sys.stdin.read())

total = 0
while n != 0:
    num = 1
    for i in range(1, n + 1):
        num *= i
    
    total += num
    n -= 1

print(total)
