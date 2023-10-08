def linear_search(arr,element):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == element:
            return i
    return -1
arr = [0,1,2,3,4,5,6,7,8]
result = linear_search(arr,8)
if  result == -1:
    print("Element is not found")
else:
    print("Element is found at index", result)