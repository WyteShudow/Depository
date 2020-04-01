import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def diction(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
       hex = input("Did you mean %s instead? Y/N: " % get_close_matches(w, data.keys())[0])
       if hex == 'Y' or hex == 'y':
           return data[get_close_matches(w, data.keys())[0]]
       elif hex == 'N' or hex == 'n':
           return "The word doesn't exist, please double check"
       else:
           return "I don't understand your query!!"
    else:
        return "The word doesn't exist, please double check"

word = input("Enter Word: ")
output = diction(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)