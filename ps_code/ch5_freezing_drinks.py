N, M = list(map(int, input().split(" "))) # N이 세로 길이, M이 가로 길이.

ice_box = []

for _ in range(N):
    each_input = input()
    temp_arr = []
    for i in range(M):
        temp_arr.append(int(each_input[i]))
    ice_box.append(temp_arr)
visited = ice_box

def dfs_visit_ice(i, j):
    if(ice_box[i][j] == 1):
        return
    else:
        visited[i][j] = 1
        if(i+1 < N and visited[i+1][j] == 0 ): # 하
            dfs_visit_ice(i+1, j)
        if(j+1 < M and visited[i][j+1] == 0): # 우
            dfs_visit_ice(i, j+1)
        if(i-1 > 0 and visited[i-1][j] == 0 ): # 좌
            dfs_visit_ice(i-1, j)
        if(j-1 > 0 and visited[i][j-1] == 0): # 상
            dfs_visit_ice(i, j-1)

        # 좌, 상 을 생각 안하고 짜서, 그것 고려한 것 까지 추가함. (테스트 케이스를 더 고려해봤어야 했는데, 그걸 안해서 발견 못한 실수.)
        
        return

icecream = 0

for ice_row in range(N):
    for ice_col in range(M):
        if(visited[ice_row][ice_col] == 0):
            dfs_visit_ice(ice_row, ice_col)
            icecream += 1

print(icecream)

