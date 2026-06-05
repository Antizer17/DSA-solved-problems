freq = {0:0}
arr = [5,2,7,6,5,5]
prefix = [0,5,7,14,20,25,30]
target = 5
for i in range (1,len(prefix)):
    x = prefix[i] - target
    if x in freq:
        print(True ,freq[x] + 1 ,i)
    else:
        freq[prefix[i]] = i
