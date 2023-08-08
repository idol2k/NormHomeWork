n = int(input('Введите номер месяца:'))
def season(num):
    if num == 1:
        return f'January', 'Zima'
    if num == 2:
        return 'February - Zima'
    if num == 3:
        return 'March - Vesna'
    if num == 4:
        return 'April - Vesna'
    if num == 5:
        return 'May - Vesna'
    if num == 6:
        return 'June - Leto'
print()