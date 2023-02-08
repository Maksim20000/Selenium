import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

urls = [
    'https://www.faceit.com/ru/shop/csgo',
    'https://www.figma.com/login',
    'https://lordserials.org/zarubezhnye/7541-horoshij-doktor-2017.html',
    'https://youtube.com/',
    'https://www.twitch.tv/',
    'https://gdz.ru',
    'https://vk.com/im?peers=648937642&amp;sel=690918218',
    'https://vk.com/b_sharnin',
    'https://fonts.google.com/',
    'https://www.freecodecamp.org/learn'
]

for i in urls:
    driver.get(i)

