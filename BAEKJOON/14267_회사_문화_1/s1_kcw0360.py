import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())
members = list(map(int, input().split()))
result = [0] * n
for _ in range(m):
    a, b = map(int, input().split())
    result[a - 1] += b

graph = [[] for _ in range(n)]
for a, b in enumerate(members):
    if b == -1:
        continue
    graph[b - 1].append(a)


def praise(boss):
    for member in graph[boss]:
        result[member] += result[members[member] - 1]
        praise(member)


praise(0)
print(*result)
