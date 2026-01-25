h1, m1, h2, m2 = map(int, input().split())

total1 = h1 * 60 + m1
total2 = h2 * 60 + m2

total = total2 - total1
hour = total // 60
minute = total - hour * 60

print(f"{hour} {minute}")