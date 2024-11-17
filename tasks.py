# 1st program
print(9 ** 0.5 * 5)

# 2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

# 3rd program
print(2 * 2 + 2)  # без приоритета
print(2 * (2 + 2))  # с приоритетом
print((2 * 2 + 2) == (2 * (2 + 2)))  # сравнение

# 4th program
number = float('123.456')  # Преобразуем строку в дробное число
number *= 10  # Смещаем запятую
first_digit_after_decimal = int(number) % 10  # Берем остаток от деления на 10
print(first_digit_after_decimal)  # Выводим первую цифру после запятой