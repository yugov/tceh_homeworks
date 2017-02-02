# Функция принимает список чисел и возвращает их произведение

def h3_4(*args):
    my_var = 1
    for arg in args:
        my_var = my_var * arg
    print(my_var)

h3_4(2, 4, 6, 10)

