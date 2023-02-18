# name = 'привте'
#
# for i in range(11):
#     print(f'прив{i}')


# for i in range(11):
#     print(f'https://platform.kodland.org/ru/change_task_{i}/')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

for i in range(1, 5, 1):
    driver.get(f'https://nekdo.ru/page/{i}/')
    time.sleep(5)


