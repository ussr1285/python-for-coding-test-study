N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for num in arr:
    print(num, end=" ")


