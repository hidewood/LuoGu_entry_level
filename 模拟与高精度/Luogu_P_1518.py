import sys

def solve():
    # 读取地图，处理可能的空行
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    my_map = [list(line) for line in lines]
    
    cow_x, cow_y, far_x, far_y = 0, 0, 0, 0
    for i in range(10):
        for j in range(10):
            if my_map[i][j] == 'F':
                far_x, far_y = i, j
            elif my_map[i][j] == 'C':
                cow_x, cow_y = i, j
    
    # 上(0), 右(1), 下(2), 左(3)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    cow_d = 0
    far_d = 0
    minutes = 0
    
    # 设定上限防止死循环 (100*100*4*4 = 160000)
    while not (cow_x == far_x and cow_y == far_y) and minutes < 160000:
        # 1. 处理农民移动
        nf_x, nf_y = far_x + dx[far_d], far_y + dy[far_d]
        # 检查是否撞墙或越界
        if not (0 <= nf_x < 10 and 0 <= nf_y < 10) or my_map[nf_x][nf_y] == '*':
            far_d = (far_d + 1) % 4
        else:
            far_x, far_y = nf_x, nf_y
            
        # 2. 处理牛移动
        nc_x, nc_y = cow_x + dx[cow_d], cow_y + dy[cow_d]
        if not (0 <= nc_x < 10 and 0 <= nc_y < 10) or my_map[nc_x][nc_y] == '*':
            cow_d = (cow_d + 1) % 4
        else:
            cow_x, cow_y = nc_x, nc_y
            
        minutes += 1
    
    if minutes >= 160000:
        print(0)
    else:
        print(minutes)

if __name__ == "__main__":
    solve()
