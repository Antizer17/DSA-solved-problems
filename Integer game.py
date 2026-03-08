def road(refuels,endpoint):
    max=0
    distance=0
    

    for i in range(endpoint+1):
        if i==0:
            continue
        distance+=1
        if str(i) in refuels:
            if distance>max:
                max=distance

            distance=0
        elif i==endpoint:
            distance*=2
    
    return max if max > distance else distance
        
tests=int(input())
for i in range(tests):
    string=input().split(" ")
    endpoint=int(string[1])  
    refuels=set(input().split(" "))
    result=road(refuels,endpoint)
    print(result)      
        