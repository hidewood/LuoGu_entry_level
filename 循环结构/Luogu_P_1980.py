n, x = map(int, input().split())

total = 0
for i in range(1, n + 1):
    num = i
    while num > 0:
        check = num % 10
        num //= 10
        if check == x:
            total += 1

print(total)

# 解法2
n, x = map(int, input().split())

total = 0
# 将 x 转为字符串，方便后续匹配
target = str(x)

for i in range(1, n + 1):
    # 将当前的数字 i 转为字符串，直接统计其中 target 出现的次数
    total += str(i).count(target)

print(total)
