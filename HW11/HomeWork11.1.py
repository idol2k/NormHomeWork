n = 3

b = 2

q = 6

def generator_geomttry(b, n, q):
    term = b
    for _ in range(q):
        yield term
        term *= n 

for progression in generator_geomttry(b, n ,q):
    print(progression)