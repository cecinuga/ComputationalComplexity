from ca_types import ComplexityAnalizerList


def generate_test_cases(n_test_case: int):
    test_case_lengths = [ test_case for test_case in range(1, n_test_case+1) ]
    test_cases = [
        ComplexityAnalizerList(
            [i for i in range(test_case_lengths[i], 0, -1)]
        ) for i in range(n_test_case)
    ]
    return {'test_case': test_cases, 'length':test_case_lengths}