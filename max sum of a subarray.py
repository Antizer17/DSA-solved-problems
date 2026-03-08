items, queries = map(int, input().split())
item_array = list(map(int, input().split()))
item_array.sort()
prefix_sum = [0]
for i in item_array:
    prefix_sum.append(prefix_sum[-1]+i)
for _ in range(queries):
    x,y = map(int, input().split())
    L = items-x
    R = L + y 
    print(prefix_sum[R]-prefix_sum[L])
    
    

   
    
        


