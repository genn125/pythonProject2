
# module_2_5.py

#  "Функции в Python. Функция с параметром"

def get_matrix  (n, m, value):

    matrix = []
    for i in range(n):

        matrix.append([])       # Добавить пустые вложенные списки в пустой список matrix

        for j in range(m):
            matrix[i].append(value)

    return matrix

print(get_matrix(2, 2, 'что угодно'))   # 2 списка по 2 шт. "value"
print(get_matrix(3, 5, [42]))   # 3 списка по 5 шт. "value"
print(get_matrix(4, 2, 13))   # 4 списка по 2 шт. "value".

