# Этот код я написал полностью сам
# Я даже не копировал плагины)



from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://127.0.0.1:5000')
time.sleep(2)

login = driver.find_element(By.NAME, 'login')
time.sleep(2)
login.click()
login.send_keys('admin')
time.sleep(2)

password = driver.find_element(By.NAME, 'password')
time.sleep(1)
password.click()
password.send_keys('admin')
time.sleep(2)

button = driver.find_element(By.TAG_NAME, 'button')
time.sleep(1)
button.click()
time.sleep(3)


#  В HTML в ссылку контакты я добавил id тк только так я могу к ней обратиться)

# <ul>
#           <li><a href="/">Главная страница</a></li>
#           <li><a href="/products">Продукция</a></li>
#           <li><a href="/contacts" id="contacts">Контакты</a></li>
#           <li><a href="/cart">Корзина</a></li>
#           <li><a href="/about">О компании</a></li>
#           <li><a href="/logout">Выход</a></li>
# </ul>

contactBtn = driver.find_element(By.ID, 'contacts')
contactBtn.click()
time.sleep(5)

