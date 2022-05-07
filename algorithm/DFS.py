def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)



graphs = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]
]


visited = [False] * 9

dfs(graphs, 1, visited)
