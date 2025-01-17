import random

def random_search(A: list[int], v: int):
    index = 0
    visited_indexes = {}
    count_visited_indexes = 0

    while ( A[index] != v and count_visited_indexes < len(A) ):
        index = random.randint(0, len(A)-1)
        if index not in visited_indexes:
            count_visited_indexes += 1 
            visited_indexes[index] = -1
            
    return index if A[index] == v else -1
