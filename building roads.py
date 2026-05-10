import sys

sys.setrecursionlimit(200000)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = 0
ambassador = []
for _ in range(m):
    n1,n2 = map(int,input().split())
    graph[n1].append((n2))
    graph[n2].append((n1))

def dfs(start):
    visited[start] =True 
    for neighbour in graph[start]:
        if visited[neighbour] == False:
            dfs(neighbour)

for i in range(1,n+1):
    if visited[i] == False:
        count += 1
        ambassador.append(i)
        dfs(i)
    else:
        continue
print(count - 1)
for i in range(1,count):
    print(ambassador[0],ambassador[i]) 