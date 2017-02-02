''' Три функции: do_work, handle_success, handle_error. do_word(my_list, success_callback, error_callback)
принимает на вход три аргумента: список, функцию для обработки успеха и функцию для обработки ошибки.
Ее задача проверить, что все значения в списке идут по-возрастанию. Если все верно: вызываем success_callback,
иначе: error_callback. Функция handle_success пишет в консоль информацию об успешном выполнении.
Функция handle_error выбрасывает ValueError
'''

def handle_success():
    print('Выполнено успешно!')
def handle_error():
    try:
        raise ValueError('Плохое значение')
    except ValueError as e:
        print(e)


def do_work(m_list, handle_success, handle_error):
    counter = 0
    for i in range(len(m_list)):
        while i < len(m_list)-1:
            if m_list[i] < m_list[i+1]:
                counter += 1
            break
    if m_list[len(m_list)-2] < m_list[len(m_list)-1]:
        counter += 1

    if counter == len(m_list):
        handle_success()
    else:
        handle_error()


good_list = [1, 2, 3, 4]
bad_list = [1, 3, 2, 4]
print('~~~~~~~~~~~~~~~~~~~~\nВызываем отсортированый список\nРезультат: ')
do_work(good_list, handle_success, handle_error)
print('~~~~~~~~~~~~~~~~~~~~\nВызываем кривой список\nРезультат: ')
do_work(bad_list, handle_success, handle_error)
