# Функция принимает список и возвращает словарь, где ключ это тип данных, значение - колличество вхождений

my_list = [1, 2,3, 'String1', 'String2', 4, 5.6, 'String3', 7.8, 3j, [14,4234]]



my_dict = {}


def types_in_list(my_super_list):
    str_count = 0
    int_count = 0
    float_count = 0
    complex_count = 0

    for i in my_super_list:
        if isinstance(i, str):
            str_count += 1
            my_dict[type(i)] = str_count
        elif isinstance(i, float):
            float_count += 1
            my_dict[type(i)] = float_count
        elif isinstance(i, int):
            int_count += 1
            my_dict[type(i)] = int_count
        elif isinstance(i, complex):
            complex_count += 1
            my_dict[type(i)] = int_count
        else:
            print('Возможно ввели tuple, dict, list:  {}'.format(i))
    return my_dict

print(types_in_list(my_list))