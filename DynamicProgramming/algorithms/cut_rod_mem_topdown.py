from typing import List

def cut_rod_mem_topdown(input: List[int], n:int=-1):
    if n == -1: n = len(input)

    memory = [-float('inf')]*n

    return cut_rod_mem_topdown_aux(input, memory, n)


def cut_rod_mem_topdown_aux(input: List[int], memory: List[int], n: int):
    if memory[n-1] >= 0: return memory[n-1]

    opt: int = 0
    if n != 0:
        opt = -float('inf')
        for i in range(0, n):
            opt = max(opt, input[i] + cut_rod_mem_topdown_aux(input, memory, n-(i+1)))

    memory[n-1] = opt
    return opt


