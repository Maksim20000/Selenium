import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from reduserce.filmRedusors import filmRedusers
from reduserce.helpRedusor import helpRedusor

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
        searchYesOrNo = int(input('Введите, пожалуйста число: '))
        if searchYesOrNo == 0:
            print('Вам нужно зайти на видио, которое вы хотите скачать')
            print('Под этим видио будет кнопка поделиться')
            print('Высвечивается ссылка, которую нужно вставить')
    #       Функция с открытием бота

        elif searchYesOrNo == 1:
            hrefVidio = input('Введите ссылку на видио: ')

            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('https://ru.savefrom.net/1-%D0%B1%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9-%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1-%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-%D1%81-youtube-160/')
            # soup = BeautifulSoup(driver.page_source, features='lxml')

            # Кнопка, которая ищет по ссылке видио
            searchVidio = driver.find_element(By.XPATH, '//*[@id="sf_url"]')
            searchVidio.send_keys(hrefVidio)

            buttonSearchVidio = driver.find_element(By.XPATH, '//*[@id="sf_submit"]')
            buttonSearchVidio.click()
            time.sleep(5)

            downloadVidio = driver.find_element(By.XPATH, '//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
            downloadVidio.click()

            time.sleep(1)
            print('20%')
            time.sleep(1)
            print('30%')
            time.sleep(1)
            print('40%')
            time.sleep(1)
            print('50%')
            time.sleep(1)
            print('70%')
            time.sleep(1)
            print('90%')
            time.sleep(1)
            print('99%')
            time.sleep(4)
            print('100%')



    else:
        print('Увы, но такой команды нет')


