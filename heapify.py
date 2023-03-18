heap_tab = [None, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]


def left(a):
    return 2 * a


def right(b):
    return 2 * b + 1


def heapify(arr, i):
    print(arr)
    l = left(i)
    r = right(i)

    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, largest)


heapify(heap_tab, 2)
