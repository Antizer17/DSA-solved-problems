n,x=map(int,input().split())
arr=list(map(int,input().split()))
counter=0
prefix_sum=[0]
entries={0:1}
for r in range(1,n+1):
    prefix_sum.append(prefix_sum[-1]+arr[r-1])
    if prefix_sum[r] - x in entries:
        counter+=entries[prefix_sum[r]-x]
    entries[prefix_sum[r]]=entries.get(prefix_sum[r],0)+1

print(counter)