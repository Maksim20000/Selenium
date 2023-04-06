# def GPT():
#     elif command == '/helpGPT':
#         print('Я вам предоставляю ChatGPT телеграмм, вам прийдется зарегистрироваться через телефон')
#         time.sleep(1)
#         # регистрация
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.get('https://web.telegram.org/k/')
#         time.sleep(10)
#
#         btnOnClickLogPhoneNum = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[3]/div/div[2]/button[1]')
#         time.sleep(1)
#         btnOnClickLogPhoneNum.click()
#
#         phoneNumber = int(input('Введите маш номер телефона без +7'))
#         phoneNumBtn = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[3]/div[2]/div[1]')
#         phoneNumBtn.send_keys(phoneNumber)
#
#         # Кнопка для того чтобы перейти к пункту где подтвержение сообщением
#         nextLevelClick = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[2]/div/div[3]/button[1]')
#         nextLevelClick.click()
#         time.sleep(2)
#
#         # куда я ввожу код подтверждения
#         message_input = driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[4]/div/div[3]/div/input')
#         code_auth = int(input('Введите код подтверждения: '))
#         message_input.click()
#         message_input.send_keys(code_auth)