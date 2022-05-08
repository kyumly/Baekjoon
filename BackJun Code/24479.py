def dfs(graph, v, visited_cnt):
    stack = [v]
    cnt = 1
    while stack:
        current = stack.pop()
        if visited_cnt[current] == 0:
            visited_cnt[current] = cnt
            cnt+=1
            for i in graph[current]:
                stack.append(i)

    for i in visited_cnt[1:]:
        print(i)


m, n, v = map(int, input().split())

graph = [[] for _ in range(m + 1)]
visited_cnt = [0 for _ in range(m + 1)]

for _ in range(n):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for node in graph:
    node.sort(reverse=True)

dfs(graph, v, visited_cnt)