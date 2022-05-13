import copy
from collections import deque

size = int(input())
graph = []

for _ in range(size):
    graph.append(list(map(int, input())))


dx = [0,0,-1,1]
dy = [1,-1, 0,0]

def bfs(graph, s, e):
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
                if (ny < 0 or ny >= size or nx < 0 or nx >= size):
                    continue
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0
                    cnt += 1
        return cnt


cntList = []
graph_copy = copy.deepcopy(graph)
for i in range(len(graph)):
    for j in range(len(graph[i])):
        temp = bfs(graph_copy, i, j)
        if temp != None:
            cntList.append(temp)

cntList.sort()
print(len(cntList))
for cnt in cntList:
    print(cnt)
