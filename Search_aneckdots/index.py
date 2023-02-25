# name = 'привте'
#
# for i in range(11):
#     print(f'прив{i}')


# for i in range(11):
#     print(f'https://platform.kodland.org/ru/change_task_{i}/')
# for i in range(1, 5, 1):
#     driver.get(f'https://nekdo.ru/page/{i}/')
#     time.sleep(5)
#
# import time
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager
# import pickle
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
#
# jockes = []
#
# for i in range(1, 3):
#     url = f'https://nekdo.ru/page/{i}/'
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, features="lxml")
#     divs = soup.findAll('div', class_='text')
#     for div in divs:
#         jock = div.text + '\n'
#         jockes.append(jock)
#     time.sleep(2)
#
# with open('anecs.pickle', 'wb') as f:
#     pickle.dump(jockes, f)


#Код чтения файла  pickle:

import pickle

favcolor = pickle.load(open("anecs.pickle", "rb"))
print(favcolor)