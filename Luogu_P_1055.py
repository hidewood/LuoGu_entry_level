isbn_str = input().strip()

nums = isbn_str.replace("-", "")
last_char = isbn_str[-1]

total = 0

for i in range(9):
    total += int(nums[i]) * (i + 1)

mod = total % 11
correct_code = 'X' if mod == 10 else str(mod)

if last_char == correct_code:
    print("Right")
else:
    print(isbn_str[:-1] + correct_code)
    