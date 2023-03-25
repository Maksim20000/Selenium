from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from reg import login2, passWord2
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
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
