N = int(input())
cnt = 0

for h in range(0, N+1):
    for m in range(0, 60):
        for s in range(0, 60):
            time = str(h) + str(m) + str(s)
            if('3' in time):
                cnt += 1

print(cnt)