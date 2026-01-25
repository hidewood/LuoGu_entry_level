import sys

# 1. 快速读取所有输入
input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])
# 如果 n 为 0 或 m 为 0 的特殊情况处理（虽然题目通常保证 m <= n）
if m == 0:
    print(0)
    exit()

# 获取所有的刺痛值
nums = list(map(int, input_data[2:]))

# 2. 初始窗口：计算前 m 个数的和
current_sum = sum(nums[:m])
min_total = current_sum

# 3. 滑动窗口：向后移动一位，减去最左边的，加上最右边的
# 这样不需要重复循环 m 次，只需 1 次加法和 1 次减法
for i in range(m, n):
    current_sum = current_sum + nums[i] - nums[i - m]
    if current_sum < min_total:
        min_total = current_sum

print(min_total)
