import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

#'html.parser' виды паксеров
#features="lxml"


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




driver.get('https://www.kodland.org/')
soup = BeautifulSoup(driver.page_source, 'html.parser')

allButtons = soup.findAll('input')

openHtmlFile = open('kd.html', 'w', encoding='UTF-8')
openHtmlFile.write(str(allButtons))
openHtmlFile.close()



soup = BeautifulSoup(html_doc, 'html.parser')
print(soup) #pretty красриво


soup = BeautifulSoup(html_doc, 'html.parser')
firstSoupeLet = soup.find('div', class_='main')
print(firstSoupeLet.prettify())
# firstSoupeLet = soup.findAll('div')
# secondSoupe = soup.find('input', _class_="input-form")


# a = soup.findAll('li')
# for i in a:
#     print(i.text)

# i = soup.find('li', class_='pip').text
# print(i)

# i = soup.find('li', class_='pip')
# print(i.text)
