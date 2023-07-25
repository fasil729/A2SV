n = int(input())
mat = [["0"] * n for i in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))

    for adj in arr[1:]:
        mat[i][adj - 1] = "1"
for s in mat:
    print(" ".join(s))