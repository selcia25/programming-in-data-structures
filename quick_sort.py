def partition(array, l, h):
    low, high = l, h
    if l!=h and l<h:
        pivot = array[l]
        low = low + 1

        while low<=high:
            if array[high] < pivot and array[low] > pivot:
                array[high],array[low] = array[low],array[high]
            if not array[low] > pivot:
                low = low+1
            if not array[high] < pivot:
                high = high - 1
        array[l],array[high] = array[high], array[l]
        return high

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)

array = [4,5,7,3,1,2]
quick_sort(array, 0, len(array)-1)
print(array)