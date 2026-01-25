left_money = 0   # 每个月的剩余储蓄
mom_money = 0    # 存在mom那里的钱

month = 1    # 记录月份
import sys
for line in sys.stdin:
    num = int(line.strip())
    left_money += 300
    # 如果预算不够了
    if left_money < num:
        print(-month)
        exit()
    
    # 如果预算充足
    ## 开销花费
    left_money = left_money - num
    
    ## 存到mom那里的钱
    mom_money += (left_money // 100) * 100
    
    left_money -= (left_money // 100) * 100
    
    month += 1
    
print(int(left_money + mom_money * 1.2))
