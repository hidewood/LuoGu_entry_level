s, v = map(int, input().split())

time_1 = (s + v - 1) // v
total_time = time_1 + 10

total_time = (24 + 8) * 60 - total_time
hour = (total_time // 60) % 24
minute = total_time % 60



# if total_time <= 480:
#     total_time = 480 - total_time
#     hour = total_time // 60
#     minute = total_time - hour * 60
# else:
#     total_time = total_time - 480
#     left_time = 24 * 60 - total_time
#     hour = left_time // 60
#     minute = left_time % 60

print(f"{hour:02d}:{minute:02d}")

# 马上需要写题解
# 改进前版本：分类处理
# 改进后版本：以前一天零点为基点，对小时进行模24处理

# **本题另外一个需要注意的点：注意打印固定位数数字的方法**