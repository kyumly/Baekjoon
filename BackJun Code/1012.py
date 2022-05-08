import copy
from collections import deque
import sys
sys.setrecursionlimit(10000)

dx = [0,0,-1,1]
dy = [1,-1, 0,0]
t = int(input())

d3 = []

def bfs(graph, s, e, row, col):
    if graph[s][e] == 0:
        return
    else :
        queue = deque([(s,e)])
        graph[s][e] = 0
        cnt = 1
        while queue:
            s,e = queue.popleft()
            for i in range(4):
                nx = s + dx[i]
                ny = e + dy[i]
                if (ny < 0 or ny >= col or nx < 0 or nx >= row):
                    continue
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0
                    cnt += 1
        return cnt

colSize = []
rowSize= []

for _ in range(t):
    m, n, count = map(int, input().split())
    init = [[0]*m for _ in range(n)]
    colSize.append(m)
    rowSize.append(n)

    for _ in range(count):
        m, n = map(int, input().split())
        init[n][m] = 1
    d3.append(init)

for d2 in range(len(d3)):
    cnt = 0
    graph = copy.deepcopy(d3[d2])
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            temp = bfs(graph, i, j, rowSize[d2], colSize[d2])
            if temp != None:
                cnt += 1
    print(cnt)

