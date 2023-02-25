N, K = list(map(int, input().split(" ")))

def until1(N, K):
    cnt = 0

    while(N > 1):
        n_k_mod = N % K
        if n_k_mod == 0:
            N /= K
            cnt += 1
        else: 
            N -= n_k_mod
            cnt += n_k_mod

    return cnt

print(until1(N, K))