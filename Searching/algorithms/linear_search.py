def linear_search(A: list[int], value: int) -> int:
    for i in range(len(A)):
        if A[i] == value:
            return i
    return None