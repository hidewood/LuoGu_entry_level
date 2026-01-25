m, t, s = map(int, input().split())

if t == 0:
    print(0)
else:
    eaten = (s + t - 1) // t
    print(m - (s + t - 1) // t)
    
