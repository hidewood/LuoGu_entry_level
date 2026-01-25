w, x, h = map(int, input().split())

q = int(input())

total = w * x * h
while q != 0:
    x1, y1, z1, x2, y2, z2 = map(int, input().split())
    
    for i in range(0, w + 1):
        for j in range(0, x + 1):
            for k in range(0, h + 1):
                if x1 <= i <= x2 and y1 <= j <= y2 and z1 <= k <= x2:
                    total -= 1

    q -= 1

print(total)
                    