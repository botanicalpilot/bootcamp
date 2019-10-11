def isOpposite(a,b):
    if a < 0 and b > 0:
        return True
    elif a > 0 and b < 0:
        return True
    else:
        return False
print(isOpposite(-1, 2))

