def find_max(arr):
    biggest = arr[0]
    for i in arr:
        if i > biggest:
            biggest = i
    return biggest

arr = [1,2,3,14,5]
print(find_max(arr))