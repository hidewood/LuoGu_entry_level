x, n = map(int, input().split())

total_dist = 0
for i in range(n):
    day = (x + i - 1) % 7 + 1
    
    if day != 6 and day != 7:
        total_dist += 250
        
print(total_dist)

# 本题的重点在于如何计算经过n天后是周几。
# 核心公式：day = (x + i - 1) % 7 + 1
