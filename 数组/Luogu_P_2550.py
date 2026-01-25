n = int(input())

nums = list(map(int, input().split()))

nums_final = [0, 0, 0, 0, 0, 0, 0]

while n != 0:
    buy_card = list(map(int, input().split()))
    
    total = 0
    for i in range(7):
        for j in range(7):
            if buy_card[i] == nums[j]:    
                total += 1
                
    if total == 7:
        nums_final[0] += 1
    elif total == 6:
        nums_final[1] += 1
    elif total == 5:
        nums_final[2] += 1
    elif total == 4:
        nums_final[3] += 1
    elif total == 3:
        nums_final[4] += 1
    elif total == 2:
        nums_final[5] += 1
    elif total == 1:
        nums_final[6] += 1
            
    n -= 1
    
for i in nums_final:
    print(i, end = " ")
    