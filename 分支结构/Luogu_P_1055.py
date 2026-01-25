isbn_str = input().strip()

# 去掉连字符，只取数字部分（前9位）
nums = isbn_str.replace("-", "")
# 最后一位校验码（可能是数字也可能是 'X'）
last_char = isbn_str[-1]

total = 0
# 使用循环或手动计算前9位
for i in range(9):
    total += int(nums[i]) * (i + 1)

mod = total % 11
# 确定正确的校验码
correct_code = 'X' if mod == 10 else str(mod)

# 判断
if last_char == correct_code:
    print("Right")
else:
    # 拼接前 12 位加上正确的校验码
    print(isbn_str[:-1] + correct_code)