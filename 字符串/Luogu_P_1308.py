import sys

# 1. 使用 sys.stdin 读入，防止 input() 自动处理掉一些特殊空格
word = sys.stdin.readline().strip().lower()
sentence = sys.stdin.readline().lower().rstrip('\r\n') # 只去掉末尾换行，保留首部空格

# 2. 核心：在首尾各加一个空格，模拟 AC 代码中的边界条件 (i==0 和 s[i+1]=='\0')
target = " " + word + " "
search_text = " " + sentence + " "

# 3. 查找
count = 0
first_pos = -1
current_pos = search_text.find(target)

while current_pos != -1:
    if first_pos == -1:
        first_pos = current_pos
    count += 1
    # 从当前位置往后继续找，注意要从匹配单词的末尾开始，防止重叠（虽然此题单词独立不重叠）
    current_pos = search_text.find(target, current_pos + 1)

if count == 0:
    print("-1")
else:
    # 因为我们在开头补了一个空格，所以得到的 current_pos 刚好抵消了 0 索引偏移
    print(f"{count} {first_pos}")
