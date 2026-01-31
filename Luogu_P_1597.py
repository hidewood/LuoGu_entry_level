s = input().strip()

a = 0
b = 0
c = 0

for i in range(len(s)):
    if i + 3 < len(s) and s[i + 3] != ':' and s[i + 3] != '=' and s[i + 3] != ';':
        if s[i] == 'a':
            if s[i + 3] >= '0' and s[i + 3] <= '9':
                a = int(s[i + 3])
            elif s[i + 3] == 'a':
                a = a
            elif s[i + 3] == 'b':
                a = b
            elif s[i + 3] == 'c':
                a = c
                
        elif s[i] == 'b':
            if s[i + 3] >= '0' and s[i + 3] <= '9':
                b = int(s[i + 3])
            elif s[i + 3] == 'a':
                b = a
            elif s[i + 3] == 'b':
                b = b
            elif s[i + 3] == 'c':
                b = c
                
        elif s[i] == 'c':
            if s[i + 3] >= '0' and s[i + 3] <= '9':
                c = int(s[i + 3])
            elif s[i + 3] == 'a':
                c = a
            elif s[i + 3] == 'b':
                c = b
            elif s[i + 3] == 'c':
                c = c

print(a, b, c)

        