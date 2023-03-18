A = [None, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]


def parent(a):
    return a // 2


def left(a):
    return 2 * a


def right(a):
    return 2 * a + 1


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
        heapify(arr, largest)


def build_heap(arr):
    for i in reversed(range(1, len(arr) // 2)):
        heapify(arr, i)


def maximum(arr):
    return A[1]


def heap_extract(arr):
    deleted = arr.pop(1)
    heapify(arr, 1)
    return deleted


def heap_increase_key(arr, i, key):
    if key < arr[i]:
        print("error, nowy klucz jest mniejszy  niż klucz aktualny!")
    arr[i] = key
    while i > 1 and arr[parent(i)] < arr[i]:
        (arr[i], arr[parent(i)]) = (arr[parent(i)], arr[i])
        i = parent(i)

def heap_insert(arr, key):
    arr.append(1)
    A_heap_size = len(arr)-1
    heap_increase_key(arr, A_heap_size, key)

build_heap(A)
"""
Aby sprawdzić działanie danej funkcji należy odkomentować linie z jej wywołaniem 
oraz (niekiedy) linię wypisującą tablicę :)  
"""
#print(A)

#print("maximum-> zwraca korzeń kopca (największą wartość): ", maximum(A))

#heap_insert(A,17)
#print("heap insert -> dodaje element do kopca i przywraca własnośc kopca max:",A)

#heap_increase_key(A, 9, 15)
#print("heap increase key-> zamienia klucz o zadanym indexie na inny i przywraca własność kopca: ", A)

#print(heap_extract(A))
#print("heap, extract -> usuwa największy element kopca i wywołuje heapify: ",A)
