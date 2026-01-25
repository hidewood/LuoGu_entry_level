n = int(input())

num = 1
for i in range(1, n + 1):  # 直接range(n)
    for j in range(1, n + 2 - i):  # 直接range(n - i)
        print(f"{num:02d}", end = "")
        num += 1
    print()

