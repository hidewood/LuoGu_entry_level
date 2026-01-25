n = int(input())

d = 1
for i in range(n):
    for j in range(n):
        print(f"{d:02d}", end = "")
        d += 1
    print()

print()
num = 1
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print("  ", end = "")
    for k in range(1, i + 1):
        print(f"{num:02d}", end = "")
        num += 1
    print()
    
