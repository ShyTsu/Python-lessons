print('Введите число:')
number = int(input())

while True:
    number = int(input('Ведите число больше 0, но меньше 10:'))
    if 1 <= number <= 9:
        print(number ** 2)
        break
    else:
        print('Читайте внимательно!')