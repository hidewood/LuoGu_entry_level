import sys

def solve():
    # 读取参数和字符串
    input_data = sys.stdin.read().split()
    if not input_data: return
    p1, p2, p3 = int(input_data[0]), int(input_data[1]), int(input_data[2])
    s = input_data[3]

    res = [s[0]]  # 先放第一个字符

    for i in range(1, len(s) - 1):
        curr = s[i]
        prev = s[i-1]
        nxt = s[i+1]

        # 判断是否符合展开条件
        if curr == '-' and nxt > prev and (
            (prev.isdigit() and nxt.isdigit()) or 
            (prev.islower() and nxt.islower())
        ):
            # 准备填充的内容
            fill_chars = []
            # 遍历中间的字符
            for code in range(ord(prev) + 1, ord(nxt)):
                char = chr(code)
                
                # p1 控制形态
                if p1 == 1:
                    target = char.lower()
                elif p1 == 2:
                    target = char.upper()
                else: # p1 == 3
                    target = '*'
                
                # p2 控制重复次数
                fill_chars.append(target * p2)
            
            # p3 控制方向
            if p3 == 2:
                fill_chars.reverse()
            
            res.append("".join(fill_chars))
        else:
            res.append(curr)

    # 加上最后一个字符（如果字符串长度大于1）
    if len(s) > 1:
        res.append(s[-1])
    
    print("".join(res))

if __name__ == "__main__":
    solve()
