import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from reg import login2, passWord2

from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
soup = BeautifulSoup(driver.page_source, features='lxml')


# progect_id = int(input('Введите id проекта: '))

time.sleep(3)

# 146548
# driver.get(f'https://hub.kodland.org/ru/project/{ progect_id }')
driver.get(f'https://hub.kodland.org/ru/project/95077')

time.sleep(10)


likes = driver.find_element(By.XPATH, '//*[@id="post-modal___BV_modal_body_"]/div[5]/div/div[1]/div[1]/span').text
comments = driver.find_element(By.XPATH, '//*[@id="post-modal___BV_modal_body_"]/div[5]/div/div[1]/div[2]/span').text
repost = driver.find_element(By.XPATH, '//*[@id="post-modal___BV_modal_body_"]/div[5]/div/div[1]/div[3]/span').text
stars = driver.find_element(By.XPATH, '//*[@id="post-modal___BV_modal_body_"]/div[5]/div/div[1]/div[4]/span').text
see = driver.find_element(By.XPATH, '//*[@id="post-modal___BV_modal_body_"]/div[5]/div/div[2]/span').text
title = driver.find_element(By.XPATH, '//*[@id="post-modal___BV_modal_body_"]/div[1]/h3').text

time.sleep(6)
spisokValues = []
for i in range(1):
    spisokValues.append(likes)
    spisokValues.append(comments)
    spisokValues.append(repost)
    spisokValues.append(stars)
    spisokValues.append(see)
    spisokValues.append(title)


likeValue, commentValue, repostValue, starsValue, seeValue, titleValue = spisokValues

print(likeValue)

# likesValue = likes.text
# commentsValue = comments.text
# reportValue = repost.text
# StarsValue = stars.text
# seeValue = see.text

# print(f'{likes}:likes')
# print(f'{comments}:comment')
# print(f'{repost}:repost')
# print(f'{stars}:stars')
# print(f'{see} :see')
# print(f'{title}, title')


time.sleep(5)










# login   //*[@id="login"]
# password    //*[@id="password"]
# btn   //*[@id="app"]/div/div[2]/div[2]/div/div/form/button

# Авторизация

# login = driver.find_element(By.XPATH, '//*[@id="login"]')
# login.click()
# login.send_keys(login2)
#
# passWord3 = driver.find_element(By.XPATH, '//*[@id="password"]')
# passWord3.click()
# passWord3.send_keys(passWord2)
#
#
# btn_reg = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/form/button')
# btn_reg.click()


