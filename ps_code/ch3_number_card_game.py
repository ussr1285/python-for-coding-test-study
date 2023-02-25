# chapter3. p.96 숫자카드게임
N, M = list(map(int, input().split(" ")))

nums = []
for _ in range(N):
    nums.append(list(map(int, input().split(" "))))

minimums = []
for row in range(N):
    minimums.append(min(nums[row]))

print(max(minimums))
