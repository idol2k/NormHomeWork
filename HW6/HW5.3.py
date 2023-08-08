spisok = ('око', 'шалаш', 'дерево', 'автомобиль', 'дед')
def mt_filter(slova):
    if(slova[::-1]) == slova:
        return mt_filter
new_tuple = filter(mt_filter, spisok)
print(list(new_tuple))        