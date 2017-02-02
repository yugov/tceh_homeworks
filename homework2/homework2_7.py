# Функция принимает любое колличество аргументов- списков и выводит список уникальных объектов

list1 = [1, 2.3, 'String1', 4]
list2 = [2.3, 1, 'String2']
list3 = ['String1', 4, 5]
list4 = [6.7, 1, 'String6', 42]

def uniq_me(*args):
    uniq_list = []
    for arg in args:
        for item in arg:
           uniq_list.append(item)
    print(set(uniq_list))

uniq_me(list1,list2,list3,list4)