import random

random_number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(arg): # функция проверки на число
    return arg.isdigit() and 1 <= int(arg) <= 100

def game(): # функция игры 
    count = 0
    while True:
        entering = input('Введите число от 1 до 100: ')
        if is_valid(entering) == False:
            print('А может быть все-таки введем целое число от 1 до 100?')
        else:
            entering = int(entering)
            if entering < random_number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif entering > random_number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                count += 1
                print(f'Вы угадали за {count} попыток, поздравляем!')
                break
            count += 1
    play_again()

def play_again(): # функция повтора игры
    while True:
        answer = input('Хотите сыграть еще раз? (y/n): ')
        if answer == 'y':
            game()
        elif answer == 'n':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        else:
            print('Некорректный ввод, попробуйте еще раз')

game()