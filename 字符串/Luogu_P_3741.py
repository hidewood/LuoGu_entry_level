n = int(input())
s = input().strip()

# 1. 先找出原本就有的 "VK"，并把它们替换成别的字符（比如 "X"）
# 这样做是为了防止修改后的字符与这些已经存在的 VK 发生冲突
temp_s = s.replace("VK", "XX")
ans = s.count("VK")

# 2. 在处理后的字符串中找 "VV" 或 "KK"
# 只要存在 "VV"，就可以把第二个 V 改成 K 变成 "VK"
# 只要存在 "KK"，就可以把第一个 K 改成 V 变成 "VK"
if "VV" in temp_s or "KK" in temp_s:
    ans += 1

print(ans)
