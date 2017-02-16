# Написать декоратор, который отменяет выполнение функции и пишет: ИМЯ_ФУНКЦИИ не будет вызвана

def antidef(my_function):
    def delfunc(*args):
        print(str(my_function.__name__), 'не будет вызвана')
    return delfunc


@antidef
def megafunc():
    print('test')


if __name__ == '__main__':
    megafunc()
