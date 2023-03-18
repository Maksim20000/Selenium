import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:5000/")

login = driver.find_element(By.NAME,  'login')
login.click()
login.send_keys('admin')
time.sleep(2)


password = driver.find_element(By.NAME, 'password')
password.click()
password.send_keys('admi')


error = driver.find_element(By.CLASS_NAME, 'login-form')
if not error:
    login = driver.find_element(By.NAME, 'login')
    login.click()
    login.send_keys('admin')
    time.sleep(5)

    password = driver.find_element(By.NAME, 'password')
    password.click()
    password.send_keys('admin')

    time.sleep(5)


button = driver.find_element(By.TAG_NAME, 'button')
button.click()

