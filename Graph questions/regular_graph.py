
def my_func():
    from collections import defaultdict


    n, m = map(int, input().split())

    graph = defaultdict(list)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    degree = len(graph[1])

    for key in graph:
        if len(graph[key]) != degree:
            return "NO"
    return "YES"

print(my_func())
        

