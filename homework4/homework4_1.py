#Реализовать класс Person, у которого должно быть два публичных поля: age и name. Также у него должен быть
# следующий набор методов: know(person), который позволяет добавить другого человека в список знакомых.
#  И метод is_known(person), который возвращает знает ли знакомы ли два человека



class Person(object):
    def __init__(self, age, name, knownlist = None):
        self.age = age
        self.name = name
        self.knownlist = []

    def known(self, person):
        self.knownlist.append(person)
        print('Person {} now known {}'.format(self.name, person.name))

    def is_known(self, person):
        if person in self.knownlist:
            print('Person {} is known {}'.format(self.name, person.name))
        else:
            print('Cant find {} in person list {}'.format(self.name, person.name))


person1 = Person(22, 'Mike')
person2 = Person(23, 'Alice')
person3 = Person(24, 'Bob')

person1.known(person2)
person1.known(person3)
person1.is_known(person2)
person2.is_known(person3)
