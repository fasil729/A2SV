n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))
    out = str(arr.count(1)) + " "
    for ind, n in enumerate(arr):
        if n:
            out += str(ind + 1) + " "
    print(out)