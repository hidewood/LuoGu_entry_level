n = int(input())

if n > 0:
    d = n
    reverse_num = 0
    
    while d != 0:
        reverse_num = reverse_num * 10 + d % 10
        d //= 10
    
    print(reverse_num)

elif n == 0:
    print(0)

else:
    n = -n
    d = n
    reverse_num = 0
    
    while d != 0:
        reverse_num = reverse_num * 10 + d % 10
        d //= 10
    
    print(-reverse_num)        