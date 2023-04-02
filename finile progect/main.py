import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

while True:
    command = input('Введите команду которую вы хотите ввести (Команда /help предоставляет все команды): ')
    if command == '/help':
        print('В моем проекте есть 3 команды:')
        time.sleep(1)
        print('1) /helpGPT - команда которая отправляет сообщение chatgpt')
        time.sleep(1)
        print('2) /film выбирает лучшие фильмы для просмотра')
        time.sleep(1)
        print('не знаю')

    elif command == '/film':
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://www.kinoafisha.info/rating/movies/')
        for i in range(10):
            titles = driver.find_element(By.CLASS_NAME, 'movieItem_title').text
            print(titles)

    elif command == '/helpGPT':
        print('Я вам предоставляю ChatGPT телеграмм, вам прийдется зарегистрироваться через телефон')
        time.sleep(1)
        # регистрация
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.telegram.org/k/')
        time.sleep(10)

        btnOnClickLogPhoneNum = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[3]/div/div[2]/button[1]')
        time.sleep(1)
        btnOnClickLogPhoneNum.click()

        phoneNumber = int(input('Введите маш номер телефона без +7'))
        phoneNumBtn = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]')
        phoneNumBtn.send_keys(phoneNumber)

        # Кнопка для того чтобы перейти к пункту где подтвержение сообщением
        nextLevelClick = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[3]/button[1]')
        nextLevelClick.click()

