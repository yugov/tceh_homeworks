# Функция принимает на вход список, если в списке все объекты - int, сортирует его. Иначе выбрасывает ValueError

def sort_int_list(*args):
    try:
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError()
        my_list  = sorted(args)
        print('Sorted list: ', *my_list)

    except ValueError:
        print('Not all int in List')


sort_int_list(1, 3, 4, 5, 12, 11)
sort_int_list('String', 1, 3, 4, 5, 12, 11)