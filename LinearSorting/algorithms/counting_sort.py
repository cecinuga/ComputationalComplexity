def counting_sort(A: list[int], k: int):
    B = [0]*len(A)
    C = [0]*(k+1)

    for j in range(len(A)):
        C[A[j]] += 1

    for i in range(len(C)):
        C[i] = C[i] + C[i-1] if i > 0 else C[i]

    for x in range(len(A)-1, -1, -1):
        B[C[A[x]]-1] = A[x]
        C[A[x]] = C[A[x]] - 1

    return B

A = [0, 2, 1, 3, 1, 1, 1]
B = counting_sort(A, 3)
print(B)