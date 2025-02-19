import random
import numpy as np
from ca_types import ComplexityAnalizerList

def generate__list_of_random_naturals__test_cases(n_test_case: int):
    test_case_lengths = [ test_case for test_case in range(1, n_test_case+1) ]
    test_cases = [
        ComplexityAnalizerList(
            random.randrange(-test_case_lengths[i], test_case_lengths[i]) for i in range(test_case_lengths[i])
        ) for i in range(n_test_case)
    ]
    return {'test_case': test_cases, 'length':test_case_lengths}

def generate__list_of_naturals__test_cases(n_test_case: int):
    test_case_lengths = [ test_case for test_case in range(1, n_test_case+1) ]
    test_cases = [
        ComplexityAnalizerList(
            [i for i in range(test_case_lengths[i], 0, -1)]
        ) for i in range(n_test_case)
    ]
    return {'test_case': test_cases, 'length':test_case_lengths}


def generate__list_of_non_sorted_integers__test_case(n_test_case: int):
    test_case_lengths = [ test_case for test_case in range(1, n_test_case+1) ]
    test_cases = [
        ComplexityAnalizerList(
            [random.randrange(-test_case_lengths[i], test_case_lengths[i]) for i in range(test_case_lengths[i])]
        ) for i in range(n_test_case)
    ]
    return {'test_case': test_cases, 'length':test_case_lengths}

def generate_horner_test_case(n_test_case: int):
    test_case_lengths = [ test_case for test_case in range(1, n_test_case+1) ]
    test_cases = [
        ( ComplexityAnalizerList(
            [i for i in range(test_case_lengths[i], 0, -1)]
        ), i) for i in range(n_test_case)
    ]
    return {'test_case': test_cases, 'length':test_case_lengths}

def generate_square_matrix_test_case(n_test_case: int):
    test_case_lengths = [ test_case for test_case in range(1, n_test_case+1) ]
    test_cases = [
        [ ComplexityAnalizerList(
            list(np.random.randint(low=0, high=256, size=(i+1,i+1)))
        ),ComplexityAnalizerList(
            list(np.random.randint(low=0, high=256, size=(i+1,i+1)))
        ) ] for i in range(n_test_case)
    ]
    return {'test_case': test_cases, 'length':test_case_lengths}

def generate_matrix_test_case(n_test_case: int):
    test_case_lengths = [ test_case for test_case in range(1, n_test_case+1) ]
    test_cases = [
        (ComplexityAnalizerList(
            list(np.random.randint(low=0, high=256, size=(i+1,i+1)))
        ), 0) for i in range(n_test_case)
    ]
    return {'test_case': test_cases, 'length':test_case_lengths}
