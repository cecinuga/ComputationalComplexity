from typing import List


def cut_rod_topdown(input: List[int], n: int=-1):
    if n == -1: n = len(input)
    if n == 0: return n

    opt = -float('inf')
    for i in range(0, n):
        opt = max(opt, input[i], cut_rod_topdown(input, n-(i+1)))

    return opt