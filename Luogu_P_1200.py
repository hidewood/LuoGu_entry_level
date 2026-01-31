planet = input().strip()

group = input().strip()

total_planet = 1
total_group = 1

for char in planet:
    total_planet *= int(ord(char) - ord('A') + 1)
    
for char in group:
    total_group *= int(ord(char) - ord('A') + 1)
    
if total_group % 47 == total_planet % 47:
    print("GO")
else:
    print("STAY")
