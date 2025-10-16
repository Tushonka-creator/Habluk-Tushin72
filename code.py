def create_square(size, symbol):
    matrix = []
    for i in range(size):
        row = []
        if i == 0 or size - i == 1:
            for j in range(size):
                row.append(symbol)
        else:
            for j in range(size):
                if j == 0:
                    row.append(symbol)
                elif size - j == 1:
                    row.append(symbol)
                else:
                    row.append(' ' * len(symbol))
        matrix.append(row)
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

def create_heart():
    word = ['у', 'н', 'и', 'к', 'у', 'м']
    wight, height = 5, 7
    matrix = [[" " for i in range(wight)] for j in range(height)]
    matrix2 = [[" " for i in range(wight)] for j in range(height)]
    pos = 3
    pos1 = 1

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0 and (j == 1 or j == 2 or j == 3):
                matrix[i][j] = "*"
            elif (i == 1 and (j == 0 or j == 4)) or (i == 2 and j == 4):
                matrix[i][j] = "*"
            elif i > 2:
                if j == pos:
                    matrix[i][j] = "*"
                    pos -= 1
                if i == 3:
                    matrix[i][0:3] = word[3:]

    for p in range(len(matrix2)):
        for q in range(len(matrix2[p])):
            if p == 0 and (q == 1 or q == 2 or q == 3):
                matrix2[p][q] = "*"
            elif (p == 1 and (q == 0 or q == 4)) or (p == 2 and q == 0):
                matrix2[p][q] = "*"
            elif p > 2:
                if q == pos1:
                    matrix2[p][q] = "*"
                    pos1 += 1
                    p += 1
                elif p == 3:
                    matrix2[p][q + 2] = "у"
                    matrix2[p][q + 3] = "н"
                    matrix2[p][q + 4] = "и"

    final_matrix = []

    for a, b in zip(matrix2, matrix):
        final_matrix.append(a + b)

    for row in final_matrix:
        for _ in row:
            print(_, end='\t')
        print()

def create_triangle(size, symbol):
    matrix = []
    row_index = 0
    for i in range(size):
        row = []
        spaces = (size - (row_index * 2 + 1)) // 2
        insight_space = size - spaces * 2 - 2
        # print(f'Spaces: {spaces}\ninsight_space: {insight_space}')
        if row_index == 0:
            for space in range(spaces):
                row.append(' ' * len(symbol))
            row.append(symbol)
            for space in range(spaces):
                row.append(' ' * len(symbol))
        elif spaces == 0:
            for j in range(size):
                row.append(symbol)
        elif spaces < 0:
            for j in range(size):
                row.append(' ' * len(symbol))
        else:
            for space in range(spaces):
                row.append(' ' * len(symbol))
            row.append(symbol)
            for space in range(insight_space):
                row.append(' ' * len(symbol))
            row.append(symbol)
            for space in range(spaces):
                row.append(' ' * len(symbol))
        matrix.append(row)
        row_index += 1
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

def create_star(size, symbol):
    matrix = []
    n = size
    for i in range(n):
        row = []
        for j in range(n):
            row.append(' ')
        matrix.append(row)
    matrix[int(n / 2)] = [symbol for i in range(n)]
    for row in matrix:
        row[int(n / 2)] = symbol
    for i in range(n):
        matrix[i][i] = symbol
    for i in range(n):
        matrix[i][n - i - 1] = symbol

    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()
      def create_rhombus(size, symbol):
    matrix = [[''for _ in range(size)]for __ in range(size)]
    x = int(size / 2)
    y = 0
    matrix[y][x] = symbol
    for _ in range(int(size / 2)):
        x += 1
        y += 1
        matrix[y][x] = symbol
    for _ in range(int(size / 2)):
        x -= 1
        y += 1
        matrix[y][x] = symbol
    for _ in range(int(size / 2)):
        x -= 1
        y -= 1
        matrix[y][x] = symbol
    for _ in range(int(size / 2)):
        x += 1
        y -= 1
        matrix[y][x] = symbol
    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()


def create_circle(size, center_x, center_y, radius):
    """
    Рисует полый круг из звёздочек в матрице заданного размера.

    Параметры:
    - size: размер квадратной матрицы (int)
    - center_x, center_y: координаты центра круга (int)
    - radius: радиус круга (int)

    Возвращает:
    - список строк, где '*' — контур круга, ' ' — пустое пространство
    """
    matrix = []

    for y in range(size):
        row = ""
        for x in range(size):
            # Вычисляем расстояние от точки (x, y) до центра
            dx = x - center_x
            dy = y - center_y
            distance_sq = dx * dx + dy * dy  # Квадрат расстояния
            radius_sq = radius * radius  # Квадрат радиуса

            # Проверяем, лежит ли точка на контуре (с допуском ±0.5 по расстоянию)
            if abs(distance_sq - radius_sq) < radius:  # Эквивалент |d - R| < 0.5
                row += "*"
            else:
                row += " "
        matrix.append(row)

    for row in matrix:
        for element in row:
            print(element, end='\t')
        print()

# create_star(7, '*')
# create_triangle(7, '*')
# create_square(7, '*')
# create_rhombus(7, '*')

while True:
    try:
        option = int(input("Введите фигуру которую нужно вывести на экран:\n"
                           "1. Квадрат\n"
                           "2. Треугольник\n"
                           "3. Круг\n"
                           "4. Ромб\n"
                           "5. Звездочка\n"
                           "6. Иван Николаевич❤️\n"))
        if option < 1 or option > 6:
            print("Введите цифру от 1 до 6")
            continue
        try:
            size = int(input("Напишите размер матрицы: "))
            symbol = input("Введите символ для заполнения: ")
            if option == 1:
                create_square(size, symbol)
            elif option == 2:
                create_triangle(size, symbol)
            elif option == 3:
                create_circle(size, 0, 0, int(size/2))
            elif option == 4:
                create_rhombus(size, symbol)
            elif option == 5:
                create_star(size, symbol)
            else:
                create_heart()
        except:
            print('Введите цифру')
            continue
    except:
        print("Введите цифру")
        continue
