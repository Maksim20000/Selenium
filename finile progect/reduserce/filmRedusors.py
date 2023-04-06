import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument("--headless")

def filmRedusers(numFilms):
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get('https://www.kinoafisha.info/rating/movies/')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    all_movies = soup.findAll('a', class_='movieItem_title')

    list_all_movies = []
    for i in range(10):
        for b in all_movies:
            list_all_movies.append(b.text)

    for i in range(1, numFilms + 1):
        time.sleep(1)
        print(f"{i} место: {list_all_movies[i]}")


