def horner_method(coefs: list[int], x: int):
    y = 0
    for i in range(len((coefs))-1, -1, -1):
        y = coefs[i] + (x * y)

    return coefs, y
