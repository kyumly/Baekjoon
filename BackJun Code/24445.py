from collections import deque

def bfs(graph, visited, s):
    queue = deque([s])
    cnt = 1
    visited[s] = cnt
    while queue:
        val = queue.popleft()
        for node in graph[val]:
            if visited[node] == 0:
                cnt += 1
                queue.append(node)
                visited[node] = cnt

    for i in visited[1:]:
        print(i)
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for node in graph:
    node.sort(reverse=True)

bfs(graph, visited, v)

