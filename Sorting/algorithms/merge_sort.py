def merge(A: list[int], p: int, q: int, r: int):
    first_len = q - p 
    second_len = r - q

    L = [0] * first_len
    R = [0] * second_len

    for i in range(first_len):
        L[i] = A[p+i]

    for j in range(second_len):
        R[j] = A[q+j]

    i, j = 0, 0

    for k in range(p, r):
        if j == len(R) or L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        elif i == len(L) or  R[j] <= L[i] :
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