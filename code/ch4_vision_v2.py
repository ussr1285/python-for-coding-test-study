N = int(input())
cnt = 0

for h in range(0, N+1):
    if('3' in str(h)):
        cnt += 60*60
        continue
    for m in range(0, 60):
        if('3' in str(m)):
            cnt += 60
            continue
        for s in range(0, 60):
            if('3' in str(s)):
                cnt += 1

print(cnt)