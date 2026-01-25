total = int(input())

if total <= 150:
    print(round(total * 0.4463, 1))
elif total <= 400:
    print(f"{150*0.4463 + (total - 150)*0.4663:.1f}")
else:
    print(round(150*0.4463+(400-150)*0.4663+(total-400)*0.5663, 1))

