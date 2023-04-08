import time
from reduserce.filmRedusors import filmRedusers
from reduserce.helpRedusor import helpRedusor
from reduserce.dlViaioRedusor import dlViaioRedusor

while True:
    command = input('Введите команду которую вы хотите ввести (Команда /help предоставляет все команды): ')
    if command == '/help':
        helpRedusor()

    elif command == '/film':
        numFilms = int(input('Топ скольки фильмов вы хотите?(до 1000): '))
        filmRedusers(numFilms)

    elif command == '/dlVidio':
        print('Я вам предоставляю возможность скачать видио с ютуба')
        time.sleep(1)
        print('Если вам понадобится инструкция как копировать ссылку на видио то введите: 0')
        time.sleep(1)
        print('А если у вас уже есть ссылка то нажмите на 1')
#       Выбор знает ли человк как качать видио
        searchYesOrNo = int(input('Введите число: '))
        if searchYesOrNo == 0:
            print('Вам нужно зайти на видио, которое вы хотите скачать')
            time.sleep(1)
            print('Под этим видио будет кнопка поделиться, нажмите на нее')
            time.sleep(1)
            print('Высвечивается ссылка на видио')
            time.sleep(1)

            hrefVidio = input('Введите эту ссылку на видио: ')
            dlViaioRedusor(hrefVidio)

        elif searchYesOrNo == 1:
            hrefVidio = input('Введите ссылку на видио: ')
            dlViaioRedusor(hrefVidio)

    else:
        print('Увы, но такой команды нет')


