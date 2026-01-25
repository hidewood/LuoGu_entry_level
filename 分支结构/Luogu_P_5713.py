n = int(input())

local_time = n * 5
luogu_time = 11 + n * 3
if local_time < luogu_time:
    print("Local")
else:
    print("Luogu")
