def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1],arr[j] = arr[j], key
            j = j - 1
        
    return arr
arr = [4,7,18,42,1,13]
print(insertion_sort(arr)) 