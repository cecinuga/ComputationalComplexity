def merge(A: list[int], p: int, q: int, r: int):
    first_len = q - p 
    second_len = r - q

    L = [0] * (first_len + 1)
    R = [0] * (second_len + 1)

    for i in range(first_len):
        L[i] = A[p+i]

    for j in range(second_len):
        R[j] = A[q+j]

    L[first_len] = float('inf')
    R[second_len] = float('inf')

    i, j = 0, 0

    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A: list[int], p: int=0, r: int=0):
    if r == 0: r = len(A)
    if p < r-1:
        q = ( p+r )//2
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)
    return A


