import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

urls = [
    'https://www.faceit.com/ru/shop/csgo',
    'https://www.figma.com/login',
]

num = 0

for i in urls:
    name = f'Site_Nomer{num}'
    # print(f'Привт,{i}')
    driver.get(i)
    page = driver.page_source
    file_ = open(f"page_{num}.html", 'w', encoding='utf-8')
    file_.write(page)
    file_.close()
    num += 1




