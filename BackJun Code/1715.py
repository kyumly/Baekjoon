import heapq

N = int(input())
array = list()
for _ in range(N):
    array.append(int(input()))

heapq.heapify(array)
sum_result = 0


while len(array) > 1:
    min = heapq.heappop(array)
    temp = heapq.heappop(array)
    sum_result += min + temp
    heapq.heappush(array, temp + min)
print(sum_result)
