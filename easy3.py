# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('Скажите ваш возраст:')
name = int(input())
if name >= 18:
    print('Доступ резрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 дет')
