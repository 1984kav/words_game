from random import choice
from popular_words import words

play = 'да'

while play == 'да':
    letters = []
    lives = 10
    word = choice(words)
    print('Я загадал слово', '*' * len(word))

    while True:
        text = ''
        letter = input('Введите букву  ')

        if letter in word:
            letters.append(letter)
        else:
            lives -= 1
            print('Ошибка!!!', end=' ')
            if lives == 0:
                print('\nВы проиграли!!!')
                print(word.upper())
                break
            else:
                print(f'Осталось {lives} жизней...')

        for i in word:
            if i in letters:
                text += i.upper()
            else:
                text += '*'
        print(text)

        if not ('*' in text):
            print('ПОБЕДА!!!')
            break

    play = input('\nХотите сыграть еще раз? [да/нет] ')

input('Нажмите ENTER для выхода...')
