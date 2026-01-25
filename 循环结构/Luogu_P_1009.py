n = int(input())

s = 0
for i in range(1, n + 1):
    j = i
    total = 1
    while j >= 1:
        total *= j
        j -= 1
    s += total

print(s)
