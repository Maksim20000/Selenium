import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pickle

driver = webdriver.Chrome(ChromeDriverManager().install())

soup = BeautifulSoup(driver.page_source, features="lxml")
url = 'https://www.python.org/downloads/'
driver.get(url)

divs = soup.find_all('span', class_='release-number')
print(divs)

# pythons = []
# for div in divs:
#     pythons.append(div.text)
#
# print(pythons)



