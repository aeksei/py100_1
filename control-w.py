# Записать условие, которое является истинным, когда целое А не кратно трем и оканчивается нулем.
n = 99
if (n % 3 == 0) and (n % 10 == 0):
    print(True)
else:
    print(False)

# Записать условие, которое является истинным, когда целое N кратно пяти и не оканчивается нулем
n = 25
if (n % 5 == 0) and (n % 10 != 0):
    print(True)
else:
    print(False)

# Ввести с клавиатуры три числа, положительные возвести в куб, а отрицательные заменить на 0.
n = [0,0,0]
n[0] = int(input('Введите число 1: '))
n[1] = int(input('Введите число 2: '))
n[2] = int(input('Введите число 3: '))

for g, i in enumerate (n):
    if i > 0:
        n[g] = i ** 3
        print(n[g])
    else:
        n[g] = 0
        print(n[g])

# Определить, является ли шестизначное число "счастливым"(сумма первых трех цифр равна сумме последних
# трех цифр).




#
# Написать программу , которая по дате рождения (день d месяц n) определяет знак Зодиака:
# с 22 марта по 21 апреля - Овен (4); с 22 апреля по 21 мая - Телец (5); с 22 мая по 21 июня - Близнецы (6);
# с 22 июня по 21 июля - Рак (7); с 22 июля по 21 августа - Лев (8); с 22 августа по 21 сентября - Дева (9);
# 22 сентября по 21 октября - Весы (10); с 22 октября по 21 ноября - Скорпион (11); с 22 ноября по 21 декабря\
# - Стрелец (12); с 22 декабря по 21 января - Козерог (1); 22 января по 21 февраля - Водолей (2); с 22 февраля
# по 21 марта - Рыбы (3).
#
# Дано вещественное число A и целое число N (> 0). Найти A в степени N: AN = A·A··A (числа A перемножаются N раз) .