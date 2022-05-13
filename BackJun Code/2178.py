import copy
from collections import deque

row, col = map(int, input().split())



dx = [0,0,1,-1]
dy = [1,-1, 0,0]
rectangle = []

for _ in range(row):
    rectangle.append(list(map(int, input())))



def bfs(graph, s, e, visited):
    visited[0][0]= 1
    if graph[s][e] == 0:
        return
    else :
        queue = deque([(s,e)])
        graph[s][e] = 0
        cnt = 1
        while queue:
            s,e = queue.popleft()
            if s == row-1 and e == col - 1:
                print(visited[s][e])
                break

            for i in range(4):
                nx = s + dx[i]
                ny = e + dy[i]
                if (ny < 0 or ny >= col or nx < 0 or nx >= row):
                    continue
                if graph[nx][ny] == 1:
                    if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                        visited[nx][ny] = visited[s][e] + 1
                        queue.append((nx, ny))



visited = [[0]*col for _ in range(row)]
bfs(rectangle, 0, 0, visited)