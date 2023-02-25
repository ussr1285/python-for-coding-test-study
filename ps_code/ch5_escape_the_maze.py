from collections import deque

N, M = list(map(int, input().split(" ")))

maze = []
for _ in range(N):
    maze.append(list(map(int, list(input()))))

que_store = deque([[0, 0, 0, maze]])
possible_result = []

def bfs_maze_escape(args_list):
    row, col, cost, visited = args_list

    visited[row][col] = 0
    cost += 1
    if(row == (N-1) and col == (M-1)):
        return cost
    else:
        # 조건에 visited로 하면, 한번 다른 경로 시뮬레이션이 지나간 거면 못 지나가는 듯. visited를 각 시뮬레이션 별로 구별하는 등으로 해야할 듯. 매개변수로 넘겨주어야 하나?
        if(row+1 < N and visited[row+1][col] == 1):
            que_store.append([row+1, col, cost, visited])
        if(row-1 >= 0 and visited[row-1][col] == 1):
            que_store.append([row-1, col, cost, visited])
        if(col+1 < M and visited[row][col+1] == 1):
            que_store.append([row, col+1, cost, visited])
        if(col-1 >= 0 and visited[row][col-1] == 1):
            que_store.append([row, col-1, cost, visited])        
        return 0

while(True):
    if(len(que_store) < 1):
        break
    temp_result = bfs_maze_escape(que_store.popleft())
    if(temp_result > 0):
        possible_result.append(temp_result)

print(min(possible_result))

''' # dfs로 시도하다가, 안될 것 같아서 bfs로 전환함.
def dfs_maze_escape(row, col, cost):
    visited[row][col] = 0
    cost += 1
    if(row == (N-1) and col == (M-1)):
        return cost
    else:
        
        if(row+1 < N and visited[row+1][col] == 1):
            return dfs_maze_escape(row+1, col, cost)
        if(row-1 >= 0 and visited[row-1][col] == 1):
            return dfs_maze_escape(row-1, col, cost)
        if(col+1 < N and visited[row][col+1] == 1):
            return dfs_maze_escape(row, col+1, cost)
        if(col-1 >= 0 and visited[row][col-1] == 1):
            return dfs_maze_escape(row, col-1, cost)

print(dfs_maze_escape(0, 0, 0))
'''


