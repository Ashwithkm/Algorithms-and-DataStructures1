#arr[] = {1, 12, -5, -6, 50, 3} , k=4

arr = [1,12,-5,-6,50,3]
k = 4
result= []
sum = 0
start = 0
for i in range(len(arr)):
    sum+=arr[i]
    
    if i>=k-1:
        result.append(sum/k)
        sum -= arr[start]
        
        start = start + 1 
print(max(result))

#time complexity = O(n)
#space complexity = O(1)
