n = int(input())

# 52*x + 21*52k

for x in range(100, 0, -1):
    for k in range(1, n):
        if 364*x + 1092*k == n:
            print(x)
            print(k)
            exit()
        elif 364*x + 1092*k > n:
            break    
