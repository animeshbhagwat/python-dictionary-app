import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(),n=1, cutoff=.6)) > 0:
        print(f'Did you mean {get_close_matches(w, data.keys(),n=1, cutoff=.6)[0]}? \n Enter y/N ')
        decision = input()
        if decision.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif decision.lower() == 'n':
            return 'The word does not exist! Please check the input.'
        else:
            return 'Invalid Input!'
    else:
        return 'The word does not exist! Please check the input.'
    
while True:
    word = input('Enter a word to translate: ')
    output = translate(word)
    if type(output) == list:
        for ele in output:
            print(ele)
    else:
        print(output)

    exit = input('Do you want to continue? y/N: ')
    if exit.lower() =='n':
        print('Thank You!')
        break
    elif exit.lower() != 'y':
        print('Invalid Input!')

    