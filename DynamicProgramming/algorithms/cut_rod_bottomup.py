from typing import List

def cut_rod_bottomup(input: List[int], n: int=-1):
    if n == -1: n = len(input)+1
    memory = [0]*(n)

    for i in range(len(memory)):
        opt = -float('inf')

        for j in range(i):
            opt = max(opt, input[j] + memory[(i-j)-1])

        memory[i] = opt if opt > 0 else 0

    return memory[-1]


