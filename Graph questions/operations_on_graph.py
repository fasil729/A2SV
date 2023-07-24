from collections import defaultdict

n = int(input())
k = int(input())
printed = []
graph = defaultdict(list)
for _ in range(k):
    arr = input().split()
    if arr[0] == "1":
        graph[arr[2]].append(arr[1])
        graph[arr[1]].append(arr[2])
    else:
        printed.append(arr[1])

for node in printed:
    print(" ".join(graph[node]))