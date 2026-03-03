n , k = input().split( )
n=int(n)
k=int(k)
arr = list(map(int, input().split()))
answer = 0
maximum=max(arr)
max_sum = sum(arr)
low = maximum
high = max_sum
while low <= high:
    mid = (high +low) // 2
    current_sum = 0
    count = 1
    for i in range(n):
        if current_sum + arr[i] <= mid:
            current_sum += arr[i]
        else:        
            print(max_sum)
            count += 1
            current_sum = arr[i]
    if count <= k:
        answer = mid
        high = mid -1       
    else:
        low = mid+1
print(answer)