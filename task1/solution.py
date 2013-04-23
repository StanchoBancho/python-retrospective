BORDERS = [19, 18, 20, 20, 20, 20, 21, 22, 22, 22, 21, 21]
SIGNS = ['Козирог', 'Водолей', 'Риби', 'Овен', 'Телец', 'Близнаци', 'Рак',
         'Лъв', 'Дева', 'Везни', 'Скорпион', 'Стрелец', 'Козирог']

def what_is_my_sign(day, month):
    if BORDERS[month-1] >= day:
        return SIGNS[month-1]
    else:
        return SIGNS[month]
