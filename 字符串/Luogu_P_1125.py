def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

s = input().strip()

nums = [0] * 26
for char in s:
    nums[ord(char) - ord('a')] += 1

max_num = max(nums)

for i in range(26):
    if nums[i] == 0:
        nums[i] = 101

min_num = min(nums)

if is_prime(max_num - min_num):
    print("Lucky Word")
    print(max_num - min_num)
else:
    print("No Answer")
    print(0)
