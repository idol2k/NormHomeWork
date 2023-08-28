first = ('First line')
second = ('Second line')


with open("line1and2.txt", "w") as my_file:
    my_file.write(first + '\n')
    my_file.write(second + '\n')

third = ('Third line')
four = ('Four line')

with open("line1and2and3and4.txt", "a") as my_new_file:
    my_new_file.write(third + '\n')
    my_new_file.write(four + '\n')