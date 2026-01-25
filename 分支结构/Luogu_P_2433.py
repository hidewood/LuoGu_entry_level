n = int(input())

if n == 1:
    print("I love Luogu!")
elif n == 2:
    print(f"{2 + 4} {10 - (2 + 4)}")
elif n == 3:
    print(14 // 4)
    print(4 * (14 // 4))
    print(14 % 4)
elif n == 4:
    v = 500 / 3
    print(f"{v:.6f}")
elif n == 5:
    print((260 + 220) // (12 + 20))
elif n == 6:
    print((6 ** 2 + 9 ** 2) ** 0.5 )
elif n == 7:
    print(100 + 10)
    print(100 + 10 - 20)
    print(0)
elif n == 8:
    print(3.141593 * 2 * 5)
    print(3.141593 * 5 * 5)
    print(4 / 3 * 3.141593 * 5 * 5 * 5)
elif n == 9:
    total = 1
    for _ in range(1, 4):
        total = (total + 1) * 2
    print(total)
elif n == 10:
    print(9)
elif n == 11:
    print(100 / 3)
elif n == 12:
    print(ord('M') - ord('A') + 1)
    print(chr(ord('A') + 17))

elif n == 13:
    v1 = 4 / 3 * 3.141593 * 4 * 4 * 4
    v2 = 4 / 3 * 3.141593 * 10 * 10 * 10
    print(int((v1 + v2) ** (1 / 3)))
    
else:
    for i in range(1, 110):
        if (110 - i) * (10 + i) == 3500:
            print(110 - i)
            break
