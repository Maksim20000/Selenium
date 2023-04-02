from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from reg import login2, passWord2

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://platform.kodland.org/auth/")

time.sleep(1)
login = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/form/div[1]/input')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/form/button')


def func2(loginOriginal, passwordOriginal):
    time.sleep(1)
    login.click()
    time.sleep(1)
    login.send_keys(Keys.CONTROL + "a")
    for i in range(len(login2)):
        login.send_keys(Keys.BACK_SPACE)
    time.sleep(1)
    login.send_keys(loginOriginal)
    time.sleep(1)

    time.sleep(1)
    password.click()
    time.sleep(1)
    password.send_keys(Keys.CONTROL + "a")
    for i in range(len(passWord2)):
        password.send_keys(Keys.BACK_SPACE)
    time.sleep(1)
    password.send_keys(passwordOriginal)
    time.sleep(1)

    time.sleep(1)
    button.click()
    time.sleep(1)


func2("admin", "some")

if driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]'):
    time.sleep(1)
    print('Web storm top')
    func2(login2, passWord2)

element = driver.find_element(By.CLASS_NAME, 'contact')
time.sleep(1)
element.click()
time.sleep(1)