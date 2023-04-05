















# returns the new pivot index
def partition(array, low, high):
    # if high <= low: return
    pivot = array[low]
    l = low + 1
    r = high
 
    while True:
        while (l <= r and array[l] <= pivot): l += 1
        while (l <= r and array[r] >= pivot): r -= 1
        if (r < l): break
        (array[r], array[l]) = (array[l], array[r])
    (array[r], array[low]) = (array[low], array[r])
    return r
 
def quickSort(array, low, high):
    print(array)
    if low < high:
        pi = partition(array, low, high)
        print(pi)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

a = [123,235646,243,52,34,2,62,5231,45]
quickSort(a, 0, len(a)-1)
print(a)