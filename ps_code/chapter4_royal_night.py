x_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = 0
possible_route = 0

position = input()

for i in range(len(x_arr)):
    if(position[0] == x_arr[i]):
        x = i+1

integer_position = (x, int(position[1]))

# 이동할 때는 최대 4*2 경우의 수.
route_list = ( # 2동1남, 2동1북, 2서1남, 2서1북, 1동2북, 1서2북, 1동2남, 1서2남
    (2, 1), (2, -1), (-2, 1), (-2, -1), (1, -2), (-1, -2), (1, 2), (-1, 2)
)

#boundary_list = ( # 북서, 북동, 남서, 남동
#    (1, 1), (8, 1), (1, 8), (8, 8)
#) 

for route in route_list:
    temp_position = tuple(sum(twin_num) for twin_num in zip(integer_position, route))
    # for boundary in boundary_list:
    if(temp_position[0] <= 8 and temp_position[0] >= 1 and temp_position[1] <= 8 and temp_position[1] >= 1):
        possible_route += 1

print(possible_route)