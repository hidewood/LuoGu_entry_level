t = int(input())

while t != 0:
    n, a = map(int, input().split())
    
    # 计算阶乘
    total = 1
    for i in range(1, n + 1):
        total *= i
    
    # 判断出现次数
    num = 0
    while total != 0:
        d = total % 10
        if d == a:
            num += 1
        total //= 10
    
    print(num)
    t -= 1