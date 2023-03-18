A = [None, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
print(A)
print("\n\n\n")

def left(a):
    return 2 * a


def right(b):
    return 2 * b + 1


def heapify(arr, i):

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
        print(arr)
        heapify(arr, largest)


def build_heap(arr):
    for i in reversed(range(1, len(arr)//2)):
        heapify(arr, i)

build_heap(A)
