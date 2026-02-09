import math
import sys

# 增加 Python 对大整数转字符串的位数限制（防止超限报错）
sys.set_int_max_str_digits(0)

def solve():
    # 读取输入的 P
    try:
        line = sys.stdin.read().split()
        if not line: return
        p = int(line[0])
    except EOFError:
        return

    # 1. 计算位数
    # log10(2) 约等于 0.3010299956639811
    digits = int(p * math.log10(2)) + 1
    print(digits)

    # 2. 计算 2^P - 1 的末 500 位
    # 使用快速幂取模计算 2^p % 10^500
    last_500 = pow(2, p, 10**500) - 1
    
    # 3. 补零并格式化输出
    res_str = str(last_500).zfill(500)
    
    for i in range(0, 500, 50):
        print(res_str[i:i+50])

if __name__ == "__main__":
    solve()
