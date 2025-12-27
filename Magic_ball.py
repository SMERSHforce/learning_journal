import random

# List of possible answers
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай","Предрешено", 
           "Вероятнее всего", "Спроси позже", "Мой ответ - нет","Никаких сомнений", "Хорошие перспективы", 
          "Лучше не рассказывать", "По моим данным - нет","Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", 
          "Перспективы не очень хорошие","Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
name = input()
print(f'Привет, {name}!')

def ask_question(): 
    #Prompt the user ask a question
    ask = input('Задай мне вопрос: ')
    #Print a random answer from the list
    print(random.choice(answers))
    #Check if the user wants to ask another question
    play_again()
    
def play_again():
    #Ask if the user wants to continue
    repeat = input('Хочешь задать еще вопрос? (y/n): ')
    if repeat == 'y':
        #If yes, restart the question loop
        ask_question()
    elif repeat == 'n':
        # If no, exit with a farewell message
        print('Возвращайся если возникнут вопросы!')
        #Handling incorrect input
    else:
        print('Некорректный ввод, попробуйте еще раз')
        
#Ask the first question
ask_question()
        