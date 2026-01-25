n, k = map(int, input().split())

total_a = 0
num_a = 0
total_b = 0
num_b = 0

for i in range(1, n + 1):
    if i % k == 0:
        total_a += i
        num_a += 1
    else:
        total_b += i
        num_b += 1

ave_a = total_a / num_a
ave_b = total_b / num_b

print(f"{ave_a:.1f} {ave_b:.1f}")
