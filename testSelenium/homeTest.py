import requests
def run_code(code):
    return eval(code)


def get_html():
    url = 'https://www.kodland.org/'
    res = requests.get(url)
    return res

def testHome():
    assert run_code('2+2') == 4
    assert run_code('2+3') == 5

