import sys
# import time

N = int(sys.stdin.readline().rstrip())
n_arr = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

M = int(sys.stdin.readline().rstrip())
m_arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

## init_time = time.time()

for m_element in m_arr:
    # m_element in n_arr 를 이진 탐색으로 구현.
    pos = [0, N // 2, N-1] # [start, mid, end]
    is_in_n = "no"
    while(pos[0] < pos[2]):
        if(n_arr[pos[1]] == m_element):
            is_in_n = "yes"
            break
        if(n_arr[pos[0]] < m_element):
            pos[0] = pos[1]
            pos[1] = (pos[2] + pos[0]) // 2 # (pos[0] + (pos[2] - pos[0])//2)
        else: # n_arr[pos[2]] > m_element
            pos[2] = pos[1]
            pos[1] = (pos[2] + pos[0]) // 2 # (pos[0] + (pos[2] - pos[0])//2)

    print(is_in_n, end=" ")
    
## tot_time = time.time() - init_time
## print(tot_time)

''' 아늬 근데 기본 라이브러리가 더 빠름. 데이터가 적어서 그런가?(기본 라이브러리가 c++로 짜여있나 그래서, 더 빠를 수도. c++로 이진탐색 짰으면 더 빠를지도?)
init_time = time.time()
for m_element in m_arr:
    if(m_element in n_arr): # 더 빠른 알고리즘 필요?
        print("yes", end=" ")
    else:
        print("no", end =" ")
    
tot_time = time.time() - init_time

print(tot_time)
'''

# no yes yes 0.0020020008087158203
# no yes yes 0.0009891986846923828