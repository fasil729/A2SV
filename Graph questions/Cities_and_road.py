n = int(input())
res = 0
for _ in range(n):
    arr = input()
    res += arr.count("1")
print(res // 2)