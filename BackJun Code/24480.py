def dfs(graph, visited, start):
    cnt = 1
    stack = [start]

    while stack:
        val = stack.pop()
        if visited[val] == 0:
            visited[val] = cnt
            cnt += 1
            for node in graph[val]:
                stack.append(node)
    for i in visited[1:]:
        print(i)
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
for node in graph:
    node.sort()

dfs(graph, visited,v)