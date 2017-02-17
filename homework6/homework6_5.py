# Написать генератор, который принимает на вход дату и на каждый вызов выдает следующий день
import datetime


def generator_date(yyyy, mm, dd):
    date = datetime.date(yyyy, mm, dd)
    while True:
        date += datetime.timedelta(days=1)
        yield date


g = generator_date(2017, 1, 17)
print(g.__next__(), g.__next__(), g.__next__())
