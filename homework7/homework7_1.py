# Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соотвественно: пишут данные в файл и читают данные из файла.


def write_to_file(data):
    file = open('testfile.txt', 'a')
    file.write(data + '\n')
    file.close()


def rear_file_data():
    file = open('testfile.txt', 'r')
    print(file.read())
    file.close()


if __name__ == '__main__':
    write_to_file('test1')
    write_to_file('test2')
    write_to_file('test3')
    rear_file_data()
