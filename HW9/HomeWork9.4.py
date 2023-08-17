class Proba:
    pass

x = Proba()


class Proba1:
    def main(r):
        r = [1, 2, 3, 4, 5]
        return type(r)

y = Proba1()

ok = Proba1.main(0)

print(ok)
print(type(x))
print(type(Proba1))
print(type(y))