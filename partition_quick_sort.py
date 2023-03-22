A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]


def partition(A, p, r):
    x = A[r - 1]
    i = p - 1
    for j in range(p, r - 2):
        if A[j] <= x:
            i += 1
            print("\n")
            print(f'tablica przed dokonaniem zamiany A= {A}')
            print(f'zamien {A[i]} z {A[j]}')
            (A[i], A[j]) = (A[j], A[i])
            print(f'iter {j} A= ', A)
        else:
            print(f'iter {j} A[j] > x')
    A[i + 1], A[r - 1] = A[r - 1], A[i + 1]
    print("x= ", x)


partition(A, 0, len(A))
print(A)
