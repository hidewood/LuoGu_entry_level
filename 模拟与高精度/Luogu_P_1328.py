import sys

n, na, nb = map(int, sys.stdin.readline().split())
lista = list(map(int, sys.stdin.readline().split()))
listb = list(map(int, sys.stdin.readline().split()))

game_list = [[0, -1, 1, 1, -1], [1, 0, -1, 1, -1], [-1, 1, 0, -1, 1], [-1, -1, 1, 0, 1], [1, 1, -1, -1, 0]]

def solve(a, b):
    return game_list[a][b]

total_a = 0
total_b = 0
for i in range (n):
    num_a = i % na
    num_b = i % nb
    
    if solve(lista[num_a], listb[num_b]) == 1:
        total_a += 1
    elif solve(lista[num_a], listb[num_b]) == 0:
        continue
    elif solve(lista[num_a], listb[num_b]) == -1:
        total_b += 1

print(total_a, total_b)