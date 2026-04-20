from collections import deque
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
parents = [ 0 for p in range(n+1)]
visited =[False] *(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs():
    for i in range(1,n+1):
        if visited[i] ==False:
            stack = deque([(i,0)])
            while stack:
                node,parent = stack.pop()
                if visited[node]:
                    continue
                else:
                    visited[node]=True

                for neighbour in graph[node]:
                    if visited[neighbour]:
                        if parents[node]!=neighbour:
                            result=[neighbour,node]
                            temp=node
                            while temp!=neighbour:
                                temp=parents[temp]
                                result.append(temp)
                            return result
                    else:
                        stack.append((neighbour,node))
                        parents[neighbour] = node
solution= dfs() 
print(' '.join(map(str,solution)))