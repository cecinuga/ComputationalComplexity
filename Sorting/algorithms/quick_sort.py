import random
import numpy as np

def partition(A: list[int], p: int, r: int) -> int:
    i = p - 1
    for j in range(p, r):
        if A[j] <= A[r]:
            i += 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp
    
    return i + 1

def random_partition(A: list[int], p: int, r: int) -> int:
    i = random.randint(p, r)
    temp = A[r]
    A[r] = A[i]
    A[i] = temp

    return partition(A, p, r)

def median_partition(A: list[int], p: int, r: int) -> int:
    indexes = [random.randint(p, r), random.randint(p, r), random.randint(p, r)]
    median = int(np.median(indexes))

    temp = A[r]
    A[r] = A[median]
    A[median] = temp

    return partition(A, p, r)


def quick_sort(A: list[int], p: int=0, r: int=float('inf')) -> list[int]:
    if r == float('inf'): r = len(A)-1

    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

def quick_sort_randomized(A: list[int], p: int=0, r: int=float('inf')) -> list[int]:
    if r == float('inf'): r = len(A)-1

    if p < r:
        q = random_partition(A, p, r)
        quick_sort_randomized(A, p, q-1)
        quick_sort_randomized(A, q, r)

def quick_sort_median(A: list[int], p: int=0, r: int=float('inf')) -> list[int]:
    if r == float('inf'): r = len(A)-1

    if p < r:
        q = median_partition(A, p, r)
        quick_sort_randomized(A, p, q-1)
        quick_sort_randomized(A, q, r)


A = [9, 8, 7, 6, 5, 4, 78, -150, 65, 8, 1, 0, 0, -895]

print(A)
quick_sort_median(A)
print(A)