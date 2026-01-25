n = int(input())

my_list = [n]
while n != 1:
    if n % 2 == 1:
        n = n * 3 + 1
        my_list.append(n)
    else:
        n //= 2
        my_list.append(n)
        
d = len(my_list)

for i in range(d - 1, -1, -1):
    print(my_list[i], end = " ")

    