# def sum(a, b):
#     return a + b

# def testSum():
#     assert sum(1, 6) == 7
#     assert sum(2, 6) == 8
#     assert sum(1, 5) == 6


# def hellow(name):
#     return 'Привет' + name

# def testHellow():
#     assert hellow('Пока') == 'ПриветПока'
#     assert hellow('привет') == 'Приветпривет'
#     assert hellow('Пока') == 'ПриветПока'
#     assert hellow('Пока') == 'ПриветПока'

import requests
# def run_code(code):
#     return eval(code)


def get_html(num):
    url = 'https://www.kodland.ru'
    res = requests.get(url)
    return res

# defl = get_html(5);
# print(defl)
# def testHome():
#     assert run_code('2+2') == 4
#     assert run_code('2+3') == 5

def test_get_html():
    assert get_html(5) == 'https://www.kodland.5'
    assert get_html(5) == 'https://www.kodland.5'
    assert get_html(5) == 'https://www.kodland.5'



