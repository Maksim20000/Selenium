import pickle
from random import choice

with open('anecs.pickle', 'rb') as f:
    data = pickle.load(f)

# print(data.keys())
# print(data)

# kids = data['дети']
# randomVChoice = choice(kids)
# print(randomVChoice)