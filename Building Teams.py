from collections import deque
n,m = map(int,input().split())
adj_list=[[] for i in range(n+1)]
teams = [0 for j in range(n+1)]


for j in range(m):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

def BFS(n):
    queue=deque()
    for b in range(1,n+1):
        if teams[b]==0:
            queue.append(b)
            teams[b] = 1
        while queue:
            node = queue.popleft()
            for k in adj_list[node]:

                if teams[k] == teams[node]:
                    return('IMPOSSIBLE')
                elif teams[k]==0:
                    teams[k]=3-teams[node]
                    queue.append(k)

    return(teams[1:])


result = BFS(n)
if result=='IMPOSSIBLE':
        print(result)
else:
    for _ in result:
        print(_,end=' ')