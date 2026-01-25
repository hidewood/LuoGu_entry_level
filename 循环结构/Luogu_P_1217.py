def check_huiwen(n):
    reverse_num = 0
    d = n
    while d != 0:
        reverse_num = reverse_num * 10 + d % 10
        d //= 10
    if n == reverse_num:
        return True
    else:
        return False

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
a, b = map(int, input().split())

for i in range(a, b + 1):
    if i > 2 and i % 2 == 0:
        continue
    else:
        if check_huiwen(i):
            if is_prime(i):
                print(i)

