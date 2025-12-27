import subprocess

print('Привет! Это главная программа, откуда будут запускаться написанные тобой модули.')
print('Список доступных модулей:')
print('1. Магический шар')
print('2. Числовая угадайка')
print('3. Генератор сложных паролей')

start = int(input('Какой модуль запустим? Введи номер: '))

if start == 1:
    subprocess.run(['python', 'Magic_ball.py'])
elif start == 2:
    subprocess.run(['python', 'Random_game.py'])
elif start == 3:
    subprocess.run(['python', 'Secure_passwords.py'])