import sys

def solve():
    # 读取输入
    line = sys.stdin.read().strip()
    if not line:
        return
    n = int(line)

    if n == 2:
        print(2)
        print(2)
        return

    # 1. 贪心拆分
    res = []
    temp_sum = 0
    i = 2
    while temp_sum + i <= n:
        res.append(i)
        temp_sum += i
        i += 1
    
    # 2. 分配剩余的差值
    remainder = n - temp_sum
    # 从后往前分配
    idx = len(res) - 1
    while remainder > 0:
        res[idx] += 1
        remainder -= 1
        idx -= 1
        if idx < 0: # 如果分了一轮还没分完，重新从最后一项开始
            idx = len(res) - 1

    # 3. 输出结果
    print(*(res)) # 解构输出，空格隔开
    
    ans = 1
    for x in res:
        ans *= x
    print(ans)

if __name__ == "__main__":
    solve()
