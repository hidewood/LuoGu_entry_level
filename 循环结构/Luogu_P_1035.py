k = int(input())

total = 0
d = 1
while k >= total:
    total += 1 / d
    d += 1
print(d - 1)

