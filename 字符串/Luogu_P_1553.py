s = input()

category = 1
# 1是整数 2是小数 3是分数 4是百分数

for char in s:
    # 先判断是否为小数
    if char == '.':
        category = 2
        break
    
    # 再判断是否为分数
    elif char == '/':
        category = 3
        break
    
    # 再判断是否为百分数
    elif char == '%':
        category = 4
        break
    
    # 最后是整数
    
if category == 1:
    rev = s[::-1]
    print(int(rev))
    
elif category == 2:
    integriry = ""
    little = ""
    cur = 1
    for char in s:
        if char == '.' and cur == 1:
            cur = 0
            continue
            
        if cur == 1:
            integriry += char
        if cur == 0:
            little += char
    
    print(f"{int(integriry[::-1])}.{int(str(int(little))[::-1])}")

elif category == 3:
    up = ""
    down = ""
    cur = 1
    for char in s:
        if char == '/' and cur == 1:
            cur = 0
            continue
        if cur == 1:
            up += char
        if cur == 0:
            down += char
    
    print(f"{int(up[::-1])}/{int(down[::-1])}")

elif category == 4:
    num = ""
    for char in s:
        if char == '%':
            break
        else:
            num += char
    
    print(f"{int(num[::-1])}%")
    


        