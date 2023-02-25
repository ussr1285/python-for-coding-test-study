def input_nums():
    return list(map(int, input().split(" ")))

def is_inside_border(simulated_pos):
    if(not(simulated_pos[0] >= 0 and simulated_pos[0] <= N and simulated_pos[1] >= 0 and simulated_pos[1] <= M )): # 범위를 벗어났는지 확인.
        return False
    return True
            
N, M = input_nums() # M이 가로, N이 세로.
current_pos = input_nums()

current_direction = current_pos[2]
current_pos = current_pos[0:2]

movement_cnt = 0

move_patterns = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 4가지 이동 패턴 = (y, x). 북동남서 순 (반시계방향) => (0, 1, 2, 3)
# borders = ((0, 0), (M-1, 0), (0, N-1), (M-1, N-1)) # 북동남서 맨 끝 순.

game_map = []

for i in range(N):
    game_map.append(input_nums())

turn_cnt = 0
while(turn_cnt < 4):
    simulated_pos = tuple(sum(temp_value) for temp_value in zip(current_pos, move_patterns[current_direction]))
    print(game_map[simulated_pos[0]][simulated_pos[1]])
    print(is_inside_border(simulated_pos))
    if(
        game_map[simulated_pos[1]][simulated_pos[0]] == 0
        and is_inside_border(simulated_pos)
    ): 
        game_map[simulated_pos[1]][simulated_pos[0]] = 1
        current_pos = [game_map[simulated_pos[1]][simulated_pos[0]][0], game_map[simulated_pos[1]][simulated_pos[0]][1]]
        movement_cnt += 1
        turn_cnt = 0
    else:
        turn_cnt += 1

    current_direction = (current_direction+1) % 4

print(movement_cnt)
