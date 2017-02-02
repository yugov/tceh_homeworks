# Функция принимает значение и обрабатывает три исключения: ValueError, TypeError или RuntimeError

l = [None]

def random_exc():
    import random
    errors = (ValueError, TypeError, RuntimeError)    # Потому что я могу
    errors_callers = ('string', 0, '1')
    my_var = random.choice(errors_callers)

    try:
         if my_var == '1':
            print(l[my_var])
         else:
            some_value = int(my_var)
            raise RuntimeError('Что то пошло не так')

    except TypeError:
        print('It\'s Type exception')
    except ValueError:
        print('It\'s Value exception')
    except RuntimeError:
        print('It\'s Runtime exception')


for i in range(10):
    print('Call number ', i + 1)
    random_exc()
    print('~~~~~~~~~~~~~~~~~~~~~~~')