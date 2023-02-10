N = int(input())
plan = list(input().split(" "))

x, y = [1, 1]

for go in plan:
    if(go == 'L' and x > 1):
        x -= 1
    if(go == 'R' and x < N):
        x += 1 
    if(go == 'U' and y > 1):
        y -= 1
    if(go == 'D' and y < N):
        y += 1

print(y, x)