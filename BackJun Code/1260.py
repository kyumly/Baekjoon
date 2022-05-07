import copy
from collections import deque

graph = [
    []
]

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        temp = queue.popleft()
        print(temp, end = ' ')
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



n, m, v = map(int ,input().split())

for _ in range(n):
    graph.append([])

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort()
    graph[e].sort()

visited = [False] * (n+1)
dfs(graph, v, copy.deepcopy(visited))
print()
bfs(graph, v, copy.deepcopy(visited))



