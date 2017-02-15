from random import choice # Для задачи 1в


#Написать списковые выражения, которые:
#создают список из строк всех нечетных чисел от 1 до 100

my_list = [str(d) for d in range(1, 100) if d % 2 != 0]

#создают список из объектов другого списка, кроме итерируемых

my_list1 = ['a, b, c', 1, 'd, e, f', 2, 3, 'q, w, e']
my_list2 = [item for item in my_list1 if not hasattr(item, '__iter__')]

#создают список из фразы 'The quick brown fox jumps over the lazy dog', где каждый объект списка - кортеж из:
#слова в верхнем регистре, слова в случанйном регистре (qUIcK) и длины слова

string1 = 'The quick brown fox jumps over the lazy dog'
list3 = [(word.upper(), ''.join([choice([i.upper(), i.lower()]) for i in word]), len(word)) for word in string1.split()]

# Написать класс IntToStr, у которого есть одно поле: value. А тип поля - число. Его задачей должно быть реализация
# возможности сложения чисел и строк. Примеры:
# obj = IntToStr(9.2)
# print(obj + 3)  # 12.2
# print('a' + obj)  # a9.2
# print(obj + 'z')  # 9.2z

class IntToStr(object):
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, str):
            return str(self.value) + other
        else:
            return self.value + other

    def __radd__(self, other):
        if isinstance(other, str):
            return other + str(self.value)
        else:
            return other + self.value

# Написать класс Stack, у которого есть два метода push(value) и pop(). Если мы пытаемся сделать pop из пустого стека,
# нужно выбрасывать исключение IndexError.

class Stack(object):
    def __init__(self):
        self.value = None
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print('Stack ', self.stack, 'added', value)

    def pop(self):
        try:
            print('Delete', self.stack.pop())
        except IndexError as e:
            print('IndexError, try', e)


# Проверка

if __name__ == '__main__':
    print('Задание 1а: ', my_list)
    print(30 * '~')
    print('Задание 1б. Первоначальный список:', my_list1, '\nРезультат:', my_list2)
    print(30 * '~')
    print('Задание 1в: ', list3)
    print(30 * '~')
    print('Задание 2:')
    obj = IntToStr(9.2)
    print(obj + 3)  # 12.2
    print('a' + obj)  # a9.2
    print(obj + 'z')  # 9.2z
    print(30 * '~')
    print('Задание 3:')
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
