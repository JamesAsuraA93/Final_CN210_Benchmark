import time


def run():
    loop = 1_000_000_000

    matrix_size = 100

    sumMatrix_A = 0
    sumMatrix_B = 0

    integerMath = 0
    floatMath = 0

    startTimeMBCounter = time.time()

    matrix_A = []
    matrix_B = []

    while integerMath <= loop:
        integerMath += (1 + 2) - (4 - 2) * ((5 * 5) / 25)

    while floatMath <= loop:
        floatMath += (1.7 + 2.1) - (4.3 - 2.5) * ((5.6 * 5.7) / 25.3)

    for i in range(matrix_size):
        temp_lst = []
        for j in range(matrix_size):
            temp_lst.append(integerMath * (j + 1))
        matrix_A.append(temp_lst)

    for i in range(matrix_size):
        temp_lst = []
        for j in range(matrix_size):
            temp_lst.append(floatMath * (j + 1))
        matrix_B.append(temp_lst)

    for i in range(matrix_size):
        for j in range(matrix_size):
            sumMatrix_A += matrix_A[i][j]
            sumMatrix_B += matrix_B[i][j]

    endTimeMBCounter = time.time()
    sec_use = endTimeMBCounter - startTimeMBCounter
    score = ((loop * 2 + matrix_size * 3) / sec_use) / 1000
    return dict(sec=float(format(sec_use, ".2f")), score=int(score))
