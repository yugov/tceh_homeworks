# Функция принимает от пользователя два значения и ищет их НОК

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))


def nok(x, y):
    if x > y:
        bigger = x
    else:
        bigger = y
    while True:
        if ((bigger % x == 0) and (bigger % y == 0)):
            nok = bigger
            break
        bigger = bigger + 1
    return nok

print('Наименьшее общее кратное: ', nok(a, b))