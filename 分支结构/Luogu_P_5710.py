x = int(input())

a = 0
b = 0
c = 0
d = 0

if x % 2 == 0 and x > 4 and x <= 12:
    a = 1
if x % 2 == 0 or (x > 4 and x <= 12):
    b = 1
if (x % 2 == 0 and (x <= 4 or x > 12)) or (x % 2 != 0 and x > 4 and x <= 12):
    c = 1
if (x % 2 != 0 and (x <= 4 or x > 12)):
    d = 1
print(f"{a} {b} {c} {d}")
