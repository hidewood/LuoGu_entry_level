s = float(input())

dis = 2.0  
step = 0

while s > 0:
    s -= dis      
    step += 1    
    dis *= 0.98   

print(step)