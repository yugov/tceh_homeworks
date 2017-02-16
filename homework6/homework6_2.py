# Реализовать декоратор, который измеряет скорость выполнения функций.
# Написать три разные функции, задекорировать их и проверить

import time


def func_to_t(my_function):
    def timer(*args):
        time1 = time.time()
        my_function()
        timer = time.time() - time1
        print('Время выполнения функци ', my_function.__name__, timer)

    return timer


@func_to_t
def func1():
    c = 1 + 2
    return c / 2


@func_to_t
def func2():
    s = 0
    for i in range(1000000):
        s += i
    return s


@func_to_t
def func3():
    stri = 'Строка'
    return stri


if __name__ == '__main__':
    func1()
    func2()
    func3()
