def task (x, y):
    if x < y:
        print(x)
        task(x + 1, y)
task(1, 10)