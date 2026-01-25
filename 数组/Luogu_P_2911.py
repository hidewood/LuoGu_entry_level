s1, s2, s3 = map(int, input().split())

nums = [0 for _ in range(s1 + s2 + s3 + 2)]

for i in range(1, s1 + 1):
    for j in range(1, s2 + 1):
        for k in range(1, s3 + 1):
            nums[i + j + k] += 1

max_target = 0
for i in range(1, s1 + s2 + s3 + 1):
    if max_target < nums[i]:
        max_target = nums[i]

for i in range(1, s1 + s2 + s3 + 1):
    if nums[i] == max_target:
        print(i)
        break
    