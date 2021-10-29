def factorial(n):
    f = 1
    for i in range(1, 2 * n + 1):
        f *= i
    return f


def degree(a, d):
    n = 1
    for i in range(d):
        n *= a
    return n


alpha = float(input('Введите точность: '))
x = int(input('\nВведите x: '))

summ = 0
n = 0
part = 0

while abs(part) > alpha or n == 0:
    part = (degree(-1, n) * (degree(x, 2 * n) / factorial(n)))
    summ += part
    n += 1

print('Сумма ряда =', summ)