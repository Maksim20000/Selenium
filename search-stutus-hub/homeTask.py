import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from reg import login2, passWord2

from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
soup = BeautifulSoup(driver.page_source, features='lxml')


# progect_id = int(input('Введите id проекта: '))

project_ids = input('Пожалуйста введите project IDs разделенные пробелом: ')
project_ids = project_ids.split(' ')

for i in project_ids:
    driver.get(f'https://hub.kodland.org/ru/project/{ i }')
    time.sleep(3)

