def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
        if not swapped:
            break 
    return arr
arr = [51,14,73,12,1]

print(bubble_sort(arr))