import requests
def get_html():
    url = 'https://www.youtube.com/'
    res = requests.get(url)
    return res

# getll_html = get_html()
#
# print(getll_html)

def test_get_html():
    assert get_html().status_code == 200