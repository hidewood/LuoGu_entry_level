k = int(input())

day = 1
total = 0
for i in range(1, k + 1):
    for j in range(1, i + 1):
        if day > k:
            break
        total += i
        day += 1

print(total)