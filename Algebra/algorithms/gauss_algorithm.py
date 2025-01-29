def print_matrix(M: list[list[int]]):
    for row in M:
        print(row)

def gauss_algorithm(M: list[list[int]]):
    for i in range(len(M)):
        if M[i][0] == 0:
            for j in range(i+1, len(M)):
                if M[j][0] != 0:
                    temp = M[i]
                    M[i] = M[j]
                    M[j] = temp
                    break
        
        for j in range(i+1, len(M)):
            if M[j][i] != 0:
                c = M[j][i]/M[i][i]
                for k in range(len(M[j])):
                    M[j][k] -= c * M[i][k]
