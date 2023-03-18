import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from reg import login2, passWord2

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://platform.kodland.org/auth/")



login = driver.find_element(By.ID, 'login')
time.sleep(1)
login.click()
login.send_keys(login2)

passWord = driver.find_element(By.ID, 'password')
passWord.click()
passWord.send_keys(passWord2)


btn = driver.find_element(By.CLASS_NAME, 'btn')
btn.click()
time.sleep(2)

btn_on_task = driver.find_element(By.XPATH, '/html/body/section[1]/div/div/div[1]/a/button')
btn_on_task.click()
time.sleep(5)


btn_xept = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[27]/div[1]')
btn_xept.click()
time.sleep(2)

btn_task_onHref = driver.find_element(By.XPATH,'//*[@id="test1"]/ul/li[27]/div[2]/div/div[1]/ul/li[6]/div/a')
btn_task_onHref.click()


# Сдать задание
btn_task_good = driver.find_element(By.XPATH, '//*[@id="sub-button"]')
btn_task_good.click()
time.sleep(2)

# готов
btn = driver.find_element(By.XPATH, '//*[@id="submit_task_button"]')
btn.click()
time.sleep(5)