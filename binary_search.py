def binary_search(array, left, right, element):
    mid = left + (right - left) // 2
    if element == array[mid]:
        return mid
    elif element < array[mid]:
        right = mid - 1
    else:
        left = mid - 1

    return -1

array = [1,2,3,4,5,6,7]
result = (binary_search(array, 0, len(array)-1, 4))
if result == -1:
    print("Element is not found")
else:
    print("Element is found at index", result)