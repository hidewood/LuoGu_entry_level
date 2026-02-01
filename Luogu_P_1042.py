import sys

game = []
game.extend(sys.stdin.read().strip())
# print(game)

left_11 = 0
right_11 = 0

left_21 = 0
right_21 = 0

for ele in game:
    if ele == 'E':
        break
    
    if ele == 'W':
        left_11 += 1
    elif ele == 'L':
        right_11 += 1
    
    if abs(left_11 - right_11) >= 2 and (left_11 >= 11 or right_11 >= 11):
        print(f"{left_11}:{right_11}")
        left_11 = 0
        right_11 = 0
print(f"{left_11}:{right_11}")

print()

for ele in game:
    if ele == 'E':
        break
    
    if ele == 'W':
        left_21 += 1
    elif ele == 'L':
        right_21 += 1
    
    if abs(left_21 - right_21) >= 2 and (left_21 >= 21 or right_21 >= 21):
        print(f"{left_21}:{right_21}")
        left_21 = 0
        right_21 = 0
print(f"{left_21}:{right_21}")

# 还是感觉到了自己的成长的，去年做这个题甚至都没做出来，当时感觉很难，现在却能够几分钟一遍过。
