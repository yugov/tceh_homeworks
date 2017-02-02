# Функция принимает любое колличество аргументов и выводит список типов принятых аргументов

def types_of_args(*args):
    list_types = []
    for i in args:
       list_types.append(type(i))
    return list_types

print(types_of_args('abc', 123, 4.56, 'def', [7.89, 10]))