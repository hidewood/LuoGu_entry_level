def solve_password():
    n = int(input().strip())
    
    s = input().strip()
    
    result = []
    
    for char in s:
        new_pos = (ord(char) - ord('a') + n) % 26
        
        new_char = chr(ord('a') + new_pos)
        result.append(new_char)
        
    print("".join(result))
    
if __name__ == "__main__":
    solve_password()
