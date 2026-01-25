n = int(input())
mini_money = 1000000000

for _ in range(1, 4):
    num, price = map(int, input().split())
    if n % num == 0:
        pencil_num = n // num
        if pencil_num * price <= mini_money:
            mini_money = pencil_num * price
    else:
        pencil_num = (n // num) + 1
        if pencil_num * price <= mini_money:
            mini_money = pencil_num * price
            
print(mini_money)