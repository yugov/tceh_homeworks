# Написать генероторное выражение, которое включает в себя все четные числа от 0 до 100

gen1 = (f for f in range(101) if f % 2 == 0)

# Проверка
for i in range(51):
    print(gen1.__next__())