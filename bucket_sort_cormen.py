import math
import sys

arr = [0.5, 0.86, 0.6, 0.7, 0.4, 0.2, 0.44, 0.22, 0.11, 0.1, 0.56, 0.33, 0.88, 0.9, 0.85, 0.0]
def insertion_sort(arr):
    for j in range(0, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key
        # print(arr)
    # print(arr)
def bucketSort(array):
    bucket = []
    n = len(array)
    for i in range(n):
        bucket.append([])
    for i in range(n):
        bucket_idx = math.floor(10 * array[i])
        bucket[bucket_idx].append(array[i])
    for i in range(n - 1):
        insertion_sort(bucket[i])
    result = []
    for i in range(n):
        result += bucket[i]
    return result


print(bucketSort(arr))
