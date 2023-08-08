def fac(n):
    if n == 0:
        return 1
    return fac(n-1)*n
print(fac(5))
print(fac(7))
print(fac(4))
print(fac(20))