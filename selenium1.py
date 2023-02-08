

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.python.org")
page = driver.page_source
file_ = open('page.html', 'w', encoding='utf-8')
file_.write(page)
file_.close()


