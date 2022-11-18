# Простой калькулятор
from colorama import init
from colorama import Fore, Back

# use Colorama to make Termcolor work on Windows too
init()
print(Fore.BLACK)
print(Back.RED)
print('Привет, я маленький калькулятор, я умею не много, но зато очень хорошо')
what = input('Познакомимся?(да,нет): ')

if what == 'да':
    name = input('Ура =^_^=, Введи своё имя:')
    age = input('А сколько тебе лет?')
    print('Привет, '+ name + '!')
    print('Тебе уже ' + str(age) + ' лет, это круто!')
else:
    print('Жаль, но мне кажется что мы знакомы')
what = input('Что делаем? (умножаем: *;   делим: /;   складываем: +;  вычитаем: -; возводим в степень **; находим '
             'корень a: #): ')
print(Back.GREEN)

a = float(input("Введите первое число: "))
b = float(input('Введите второе число: '))

if what == '+':
    c = a + b

    print(Back.CYAN)

    print('Результат = ' + str(c))
elif what == '-':
    c = a - b
    print(Back.CYAN)
    print('Результат = ' + str(c))
elif what == '*':
    c = a * b
    print(Back.RED)
    print('Результат = ' + str(c))
elif what == '/':
    c = a / b
    print(Back.YELLOW)
    print('Результат = ' + str(c))
elif what == '**':
    c = a ** b
    print(Back.YELLOW)
    print('Результат = ' + str(c))
elif what == '#':
    num = a
    sqrt = num ** (0.5)
    print('Результат = ' + str(sqrt))
else:
    print('Выбрана неверная операция')
input()