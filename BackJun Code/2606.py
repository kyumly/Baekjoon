from collections import deque

def bfs(grahp, start, visited):
    cnt = 0
    queue = deque([start])

    visited[start] = True
    while queue:
        v = queue.popleft()
        #print(v, end = ' ')

        for i in grahp[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt = cnt+1

    return cnt

graph = [
    []
]

r = int(input())
line = int(input())

for _ in range(r):
    graph.append([])


for _ in range(line):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort()
    graph[e].sort()


visited= [False] * (r+1)
print(bfs(graph, 1, visited))
