import random

A = [2, 8, 7, 1, 3, 5, 6, 4]

print("A=", A)
def partition(arr, p, r):
    x = arr[r]  # element rozdzielający
    i = p - 1
    for j in range(p, r, 1):
        if arr[j] <= x:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
    return i + 1


def randomized_partition(arr, p, r):
    i = random.randrange(p, r)
    (arr[r], arr[i]) = (arr[i], arr[r])
    return partition(arr, p, r)


def randomized_quick_sort(arr, p, r):
    if p < r:
        q = randomized_partition(arr, p, r)
        randomized_quick_sort(arr, p, q - 1)
        randomized_quick_sort(arr, q + 1, r)

randomized_quick_sort(A, 0, len(A)-1)
print("sorted A=", A)
