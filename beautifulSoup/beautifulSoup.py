from bs4 import BeautifulSoup

html_doc = """
<html>

<head>
    <title>
        example
    </title>
</head>

<body>
    <ul>
        <li class = 'pip'>Главная страница</li>
        <li>Товары</li>
        <li>Контакты</li>
        <li>Корзина</li>
    </ul>
    <div>
        <p>Информация о чем то тут..</p>
        <p>И тут..</p>
    </div>
    <div class='main'>
        <input type="text" placeholder="Напиши" class="input-form">
    </div>
</body>

</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# firstSoupeLet = soup.findAll('div')
# secondSoupe = soup.find('input', _class_="input-form")


# a = soup.findAll('li')
# for i in a:
#     print(i.text)

# i = soup.find('li', class_='pip').text
# print(i)

# i = soup.find('li', class_='pip')
# print(i.text)
