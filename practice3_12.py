def makeFib(n):
    growingFib = [0, 1, ]
    rangeN = [i for i in range(n + 1)]
    for N in rangeN:
        if N >= 2:
            a = growingFib[-1] + growingFib[-2]
            growingFib.append(a)
    return growingFib
print(makeFib(15))

