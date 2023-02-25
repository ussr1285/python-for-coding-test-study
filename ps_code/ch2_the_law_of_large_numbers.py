N, M, K = list(map(int, input().split(' ')))
nums = list(map(int, input().split(' ')))
total = 0

def find_big(nums):
    big = [0, 0]

    for num in nums:
        if num >= big[0]:
            big[1] = big[0]
            big[0] = num
    return big

big = find_big(nums)

i = 0
while (i < M):
    for temp_m in range(K):
        if i >= M:
            break
        total += big[0]
        i += 1
    if i >= M:
        break
    total += big[1]
    i += 1

print(total)