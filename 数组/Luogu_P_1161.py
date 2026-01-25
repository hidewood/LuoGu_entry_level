import sys

n = int(input())

light_state = [0] * 2000000
while n != 0:
    nums = input().split()
    if not nums: continue
    
    a = float(nums[0])
    t = int(nums[1])
    
    for i in range(1, t + 1):
        if light_state[int(a * i)] == 1:
            light_state[int(a * i)] = 0
        else:
            light_state[int(a * i)] = 1

    n -= 1
    
for i in range(2000000):
    if light_state[i] == 1:
        print(i)
    
