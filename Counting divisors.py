import math
n=int(input())
limit=10**6
counter=0
spf_arr=[1]*(limit+1)

for i in range(2,limit**0.5+1):
    if spf_arr[i]==1:
     for j in range(i*i,limit+1,i):
         if spf_arr[j]==1:
            spf_arr[j]=i
           
            

divisors=1

for i in range(n):  
    q=int(input())
    while q!=1:
        
        if spf_arr[q]==1:
            temp_spf=q
        else:
            temp_spf=spf_arr[q]
            
        while q%temp_spf ==0:
            
            q=q//temp_spf
            counter+=1
        divisors*= counter+1
        counter=0
    
    
    print(divisors)
    divisors=1