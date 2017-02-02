#  Функция принимает словарь, преобразует все ключи словаря к строкам и возвращает новый словарь


def key_to_string(my_dict):
    new_dict = {}

    for key, value in my_dict.items():
        if not isinstance(key, str):
            key = str(key)
        new_dict.update({key: value})
    print(new_dict)


megadict = {'key1': 1234, 2: 5678, 'key3': 'String1', 'key4': 9.10, 'key6': 'String2', 'key7': 'String3'}
key_to_string(megadict)