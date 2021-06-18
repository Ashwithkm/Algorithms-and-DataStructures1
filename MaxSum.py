arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4 
result = []
start = 0
if len(arr)<k:
    print("Invalid")
else:
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if i >= k-1:
            result.append(sum)
            sum -= arr[start]
            start = start + 1
        
print(max(result))

#time complexity = O(n)
#space complexity = O(1)
