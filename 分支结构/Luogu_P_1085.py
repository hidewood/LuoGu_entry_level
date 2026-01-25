angry_most_day = 0
most_class_time = 0
    
for i in range(1, 8):
    school, mom = map(int, input().split())
    
    if school + mom > 8 and most_class_time < school + mom:
        angry_most_day = i
        most_class_time = school + mom
    
print(angry_most_day)

# 虽然是道入门题，但是思维上还是有很多值得回味的地方。

