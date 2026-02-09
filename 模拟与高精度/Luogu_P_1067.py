import sys

def solve():
    # Read n and the coefficients
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    coeffs = list(map(int, input_data[1:]))
    
    first_term = True # Flag to track the first term being printed

    for i in range(len(coeffs)):
        c = coeffs[i]
        power = n - i
        
        if c == 0:
            continue
        
        # 1. Handle the Sign
        if c > 0:
            if not first_term:
                print("+", end="")
        else: # c < 0
            print("-", end="")
        
        # 2. Handle the Coefficient Magnitude
        # Only print the number if:
        # - It's not 1 or -1
        # - OR it's the constant term (power == 0)
        abs_c = abs(c)
        if abs_c != 1 or power == 0:
            print(abs_c, end="")
        
        # 3. Handle the 'x' and Power
        if power > 0:
            print("x", end="")
            if power > 1:
                print(f"^{power}", end="")
        
        first_term = False
    print() # New line at the end

if __name__ == "__main__":
    solve()
