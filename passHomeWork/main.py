import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from reg import login2, passWord2

# driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver/", options=chrome_options)
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
time.sleep(2)
btn.click()
time.sleep(5)


# error = driver.find_element(By.CLASS_NAME, 'message message--error')

# if error:
#     login = driver.find_element(By.ID, 'login')
#     time.sleep(1)
#     login.click()
#     login.send_keys(login2)
#
#     passWord = driver.find_element(By.ID, 'password')
#     passWord.click()
#     passWord.send_keys(passWord2)
#
#     btn = driver.find_element(By.CLASS_NAME, 'btn')
#     time.sleep(2)
#     btn.click()
#     time.sleep(5)

# btn_on_task = driver.find_element(By.CLASS_NAME, 'primary-btn')
# btn_on_task.click()
# time.sleep(2)
#
# activate_lesson = driver.find_element(By.CLASS_NAME, 'lesson-wrapper active')
# activate_lesson.click()
# time.sleep(5)

driver.get('https://platform.kodland.org/ru/task_56519/')
time.sleep(5)

textAreaTask = driver.find_element(By.TAG_NAME, 'textarea')
textAreaTask.send_keys('Это задание сдано роботом')
time.sleep(2)

passTask = driver.find_element(By.ID, 'sub-button')
passTask.click()
time.sleep(5)


good = driver.find_element(By.ID, 'submit_task_button')
good.click()
time.sleep(10)

