# dlViaioRedusor
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# def dlViaioRedusor(hrefVidio):
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get('https://ru.savefrom.net/1-%D0%B1%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9-%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1-%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-%D1%81-youtube-160/')
#
#     # Кнопка, которая ищет по ссылке видио
#     searchVidio = driver.find_element(By.XPATH, '//*[@id="sf_url"]')
#     searchVidio.send_keys(hrefVidio)
#
#     buttonSearchVidio = driver.find_element(By.XPATH, '//*[@id="sf_submit"]')
#     buttonSearchVidio.click()
#     time.sleep(5)
#
#     downloadVidio = driver.find_element(By.XPATH, '//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
#     downloadVidio.click()
#
#     time.sleep(1)
#     print('20%')
#     time.sleep(1)
#     print('30%')
#     time.sleep(1)
#     print('40%')
#     time.sleep(1)
#     print('50%')
#     time.sleep(1)
#     print('70%')
#     time.sleep(1)
#     print('90%')
#     time.sleep(1)
#     print('99%')
#     time.sleep(4)
#     print('100%')
#     time.sleep(2)
#     print('Это видио сохранено на ваш компьютер в раздел загрузки')
#


# https://www.youtube.com/shorts/jhZylcNsrQM

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

def dlViaioRedusor(hrefVidio):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://ru.savefrom.net/1-%D0%B1%D1%8B%D1%81%D1%82%D1%80%D1%8B%D0%B9-%D1%81%D0%BF%D0%BE%D1%81%D0%BE%D0%B1-%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-%D1%81-youtube-160/')

    # Кнопка, которая ищет по ссылке видио
    searchVidio = driver.find_element(By.XPATH, '//*[@id="sf_url"]')
    searchVidio.send_keys(hrefVidio)

    buttonSearchVidio = driver.find_element(By.XPATH, '//*[@id="sf_submit"]')
    buttonSearchVidio.click()
    time.sleep(5)

    downloadVidio = driver.find_element(By.XPATH, '//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
    downloadVidio.click()

    time.sleep(1)
    print('20%')
    time.sleep(1)
    print('30%')
    time.sleep(1)
    print('40%')
    time.sleep(1)
    print('50%')
    time.sleep(1)
    print('70%')
    time.sleep(1)
    print('90%')
    time.sleep(1)
    print('99%')
    time.sleep(4)
    print('100%')
    time.sleep(2)
    print('Это видио сохранено на ваш компьютер в раздел загрузки')