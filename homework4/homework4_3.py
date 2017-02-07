# Написать класс Animal и Human, сделать так, чтобы некоторые животные были опасны для человека (хищники, ядовитые).
# Другие - нет. За что будет отвечать метод is_dangerous(animal)

class Human(object):
    def is_dangerous(self, animal):
        if animal.dng:
            print('Животное опасно')
        else:
            print('Животное не опасно')


class Animal(object):  # Не опасны
    dng = False


class Predator(Animal):  # Хищники не опасны
    pass

class Poisonous(Animal):   # Ядовитые опасны
    dng = True


hmn = Human()


anm1 = Predator()
anm2 = Poisonous()
anm3 = Animal()
hmn.is_dangerous(anm1)
hmn.is_dangerous(anm2)
hmn.is_dangerous(anm3)
