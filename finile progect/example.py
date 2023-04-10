import requests
def ask_wikipedia_question(question):
    API_URL = 'https://7012.deeppavlov.ai/model'
    data = {'question_raw':  [question]}
    res = requests.post(API_URL, json=data).json()

    return res[0][0]

print(ask_wikipedia_question(''))

