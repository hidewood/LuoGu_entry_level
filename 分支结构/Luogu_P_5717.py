a, b, c = map(int, input().split())

if a + b <= c or a + c <= b or b + c <= a:
    print("Not triangle")
else:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Right triangle")
    if a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print("Acute triangle")
    if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        print("Obtuse triangle")
    if a == b or b == c or c == a:
        print("Isosceles triangle")
    if a == b and b == c:
        print("Equilateral triangle")
    


