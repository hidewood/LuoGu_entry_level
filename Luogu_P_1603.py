s = input().split()

dict_num = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16,
    "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,

    # 非正规
    "a": 1, "another": 1, "first": 1,
    "both": 2, "second": 2,
    "third": 3
}

res = []

for word in s:
    word = word.strip('.')   # 去掉句号
    if word in dict_num:
        x = dict_num[word]
        val = (x * x) % 100
        res.append(f"{val:02d}")  # 两位数

# 如果没有任何数字
if not res:
    print(0)
else:
    res.sort()
    ans = "".join(res).lstrip('0')
    print(ans if ans else 0)
