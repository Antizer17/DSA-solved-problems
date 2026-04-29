import math
import heapq
n,m = map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[math.inf for _ in range(n+1)]
parents=[-1 for _ in range(n+1)]
distance[1]=0
pq=[]
heapq.heappush(pq,(0,1))

for i in range(m):
    node1,node2,weight=map(int,input().split())
    graph[node1].append((weight,node2))
    graph[node2].append((weight,node1))
while pq:
    weight,node=heapq.heappop(pq)
    if weight>distance[node]:
        continue
    for u,v in graph[node]:
        if distance[v]>distance[node]+u:
            distance[v]=distance[node] + u
            parents[v]=node
            heapq.heappush(pq,(distance[v],v))
        

if distance[n]==math.inf:
    print('-1')
else:  
    temp=n
    arr=[]
    while temp!=-1:
        arr.append(temp)
        temp=parents[temp]

    arr.reverse()
    print(" ".join(map(str,arr)))
