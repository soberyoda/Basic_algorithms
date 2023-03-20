A = [2, 8, 7, 1, 3, 5, 6, 4]


def quick_sort(arr, p, r):
    if p < r:
        print("\n", arr)
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)



def partition(arr, p, r):
    x = arr[r]  # element rozdzielający
    i = p - 1
    for j in range(p, r, 1):
        if arr[j] <= x:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[r]) = (arr[r], arr[i + 1])
    return i + 1


quick_sort(A, 0, len(A) - 1)
print("\nsorted: ", A)
