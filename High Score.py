import math
n,m = map(int,input().split())
edges=[]
distance = [-math.inf for _ in range(n+1)]
distance[1]=0
for _ in range(m):
        node1,node2,weight = map(int,input().split())
        edges.append((node1,node2,weight))
for i in range(n-1):
    for j in range(m):
        if distance[edges[j][0]]!=-math.inf:
            if distance[edges[j][1]]<distance[edges[j][0]] + edges[j][2]:     
                distance[edges[j][1]] = distance[edges[j][0]] + edges[j][2]

for i in range(n-1):
    for j in range(m):
        if distance[edges[j][0]]!=-math.inf:
            if distance[edges[j][1]]<distance[edges[j][0]] + edges[j][2]:     
                distance[edges[j][1]] = math.inf


if distance[-1]==math.inf:
    print(distance[-1])
else:
    print(int(distance[-1]))

