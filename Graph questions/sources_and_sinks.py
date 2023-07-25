n = int(input())
sinks = []
not_sources = set()

for i in range(n):
    arr = list(map(int, input().split()))
    if arr.count(1) == 0:
        sinks.append(str(i + 1))
    for ind, val in enumerate(arr):
        if val == 1:
            not_sources.add(ind + 1)
sources = [str(n - len(not_sources))]
for i in range(n):
    if i + 1 not in not_sources:
        sources.append(str(i + 1))
print(" ".join(sources))
print(str(len(sinks)), " ".join(sinks))

