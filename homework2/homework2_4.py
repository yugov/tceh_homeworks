# Функция принимает на вход 2 словаря и выводит общее колличество ключей
dict1 = {'key1': 1234, 'key2': 5678, 'key3': 'String1', 'key4': 9.10, 'key6': 'String2', 'key7': 'String3'}
dict2 = {'key1': 1112, 'key2': 1314, 'key3': 'String4', 'key5': 'String5', 'key8': 'String6'}


def keys_finder(d1, d2):
    count = 0
    for i in d1.keys():
        for j in d2.keys():
            if i == j:
                count += 1
    return count

print('Общее колличество ключей: ',keys_finder(dict1, dict2))
