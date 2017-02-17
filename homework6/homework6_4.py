# Написать генератор, который возвращает бесконечную последовательность случайных чисел,
# таких что следующее не меньше прошлого
import sys, random


def generator():
    first = -1 * sys.maxsize
    while first < sys.maxsize:
        first = random.randint(first, sys.maxsize)
        yield first


if __name__ == '__main__':
    g = generator()
    print(g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(),
          g.__next__(), )
