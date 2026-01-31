my_list = input()
# print(my_list)

total = 0
for char in my_list:
    if char == ' ' or char == 'a' or char == 'd' or char == 'g' or char == 'j' or char == 'm' or char == 'p' or char == 't' or char == 'w':
        total += 1
    if char == 'b' or char == 'e' or char == 'h' or char == 'k' or char == 'n' or char == 'q' or char == 'u' or char == 'x':
        total += 2
    if char == 'c' or char == 'f' or char == 'i' or char == 'l' or char == 'o' or char == 'r' or char == 'v' or char == 'y':
        total += 3
    if char == 's' or char == 'z':
        total += 4
print(total)
word = input().strip().lower()

sentence = input().lower()

target = " " + word + " "
search_text = " " + sentence + " "

total = search_text.count(target)

if total == 0:
    print("-1")
else:
    pos = search_text.find(target)
    print(f"{total} {pos}")
