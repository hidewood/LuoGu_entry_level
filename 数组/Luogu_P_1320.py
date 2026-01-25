import sys

# 1. 读取所有输入并合并成一个长字符串
# sys.stdin.read().split() 会自动处理空格和换行
raw_data = sys.stdin.read().split()
if not raw_data:
    exit()

# 获取矩阵边长 N (第一行的长度)
n = len(raw_data[0])
# 合并所有行得到完整的 01 序列
all_bits = "".join(raw_data)
# print(all_bits)

# 2. 统计连续的 0 和 1
answer = [n]           # 第一个数字输出 N
current_target = '0'   # 必须从统计 '0' 开始
count = 0

for bit in all_bits:
    if bit == current_target:
        count += 1
    else:
        # 遇到不同的字符，记录当前计数，切换目标并重置计数
        answer.append(count)
        current_target = '1' if current_target == '0' else '0'
        count = 1
        
# 把最后残留的计数加上
answer.append(count)

# 3. 按要求输出结果
print(*(answer))
