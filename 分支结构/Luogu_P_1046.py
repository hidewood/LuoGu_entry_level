height = list(map(int, input().split()))
taotao = int(input())
max_height = taotao + 30

height.sort()

nums = 0
for i in range(10):
    if height[i] <= max_height:
        nums += 1

print(nums)

