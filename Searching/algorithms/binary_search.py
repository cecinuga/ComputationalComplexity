def binary_search(A: list[int], value: int, l:int=0, c:int=0, r:int=0) -> int:
    if r == 0: r = len(A[l:])
    if c == 0: c = (r-l)//2
    if len(A[l:r]) == 0: return None

    if A[c] < value:
        return binary_search(A, value, c+1, c+(r-c+1)//2, r)
    elif A[c] > value: 
        return binary_search(A, value, l, l+(c-l)//2, c)
    else: return c