n = int(input())
score_list = []
for _ in range(n):
    score_list.extend(map(int, input().split()))

total = 0
# i 代表每个人的语文成绩所在的索引：0, 3, 6...
for i in range(0, n * 3, 3):
    # j 从 i 的下一个人开始对比
    for j in range(i + 3, n * 3, 3):
        # 语文差值
        if abs(score_list[i] - score_list[j]) <= 5 and \
           abs(score_list[i+1] - score_list[j+1]) <= 5 and \
           abs(score_list[i+2] - score_list[j+2]) <= 5:
            # 总分差值
            sum1 = score_list[i] + score_list[i+1] + score_list[i+2]
            sum2 = score_list[j] + score_list[j+1] + score_list[j+2]
            if abs(sum1 - sum2) <= 10:
                total += 1
print(total)
