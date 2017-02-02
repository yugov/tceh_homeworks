# Функция принимает матрицу ( список списков ) и выводит в консоль построчно

matrix = [ [1,2,3], [4,5,6], [7,8,9]]

def matrix_out(m):
    for row in m:
        print(row)

matrix_out(matrix)
