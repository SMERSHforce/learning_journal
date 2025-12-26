import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

def main(): #общий массив символов
    chars = ''
    quantity = int(input('Сколько паролей нужно? '))
    lenght = int(input('Какой длины должен быть пароль? '))
    in_digits = input('Включать ли цифры? (y/n) ')
    in_lowercase = input('Включать ли прописные буквы? (y/n) ')
    in_uppercase = input('Включать ли строчные буквы? (y/n) ')
    in_punctuation = input('Включать ли символы? (y/n) ')
    ambiguous = input('Исключить ли неоднозначные символы (il1Lo0O)? (y/n) ')
    
    if in_digits == 'y':
        chars += digits
    if in_lowercase == 'y':
        chars += lowercase_letters
    if in_uppercase == 'y':
        chars += uppercase_letters
    if in_punctuation == 'y':
        chars += punctuation
    if ambiguous == 'y':
        chars = ''.join([c for c in chars if c not in 'il1Lo0O'])
    
    if not chars:
        print('Ошибка: нужно выбрать хотя бы один тип символов!')
        return
    
    for _ in range(quantity):
        password = ''.join(random.sample(chars, lenght))
        print(password)
        
main()