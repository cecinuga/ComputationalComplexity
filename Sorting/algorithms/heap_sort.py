def left(i: int):
    return i*2

def right(i: int):
    return i*2+1

def max_heapify(A: list[int], i: int, heap_size: int):
    l = left(i)
    r = right(i)

    if l < heap_size and A[l] > A[i]:
        max = l
    else: max = i

    if r < heap_size and A[r] > A[max]:
        max = r

    if max != i:
        temp = A[i]
        A[i] = A[max]
        A[max] = temp

        max_heapify(A, max, heap_size)

def build_max_heap(A: list[int]):
    heap_size = len(A)
    for i in range((len(A)//2)-1, -1, -1):
        max_heapify(A, i, heap_size)
    return heap_size

def heap_sort(A: list[int]):
    heap_size = build_max_heap(A)
    for i in range(len(A)-1, 0, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heap_size -= 1

        max_heapify(A, 0, heap_size) 
    return A



