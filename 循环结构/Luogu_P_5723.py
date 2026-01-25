l = int(input())

def is_prime(n):
    if n < 2:
        return False
    # Check for factors up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = 0
x = 2
# Loop continues only as long as the next potential smallest prime can fit
while x <= l:
    if is_prime(x):
        print(x)
        num += 1
        l -= x
    x += 1

print(num)
