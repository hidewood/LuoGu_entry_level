s = input().split()
print(int(s[0]) + int(s[1]))

# 统计几种python输入方式
## 1. 本题中提供的方式——可以输入多个数字
"""
s = input().split()
print(int(s[0]) + int(s[1]))

"""

## 2. map方式——两个元素
"""
a, b = map(int, input().split())

"""

## 3. map方式——多个元素
"""
nums = list(map(int, input().split()))

"""









