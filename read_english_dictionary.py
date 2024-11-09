# https://github.com/dwyl/english-words?tab=readme-ov-file
import json
from random import sample

f = open('data/scrabble_dictionary.json')

d = json.load(f)

print(d)

# print(list(d)[0:100])
# print('goodbye' in d)