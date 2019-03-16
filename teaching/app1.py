import json
from difflib import get_close_matches

 # library index HTML => list of STL

data = json.load(open("data.json", 'r'));

def translate(w):
    w = w.lower()
    if w in data:
        return data[w];
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead ? Enter Y if yes, or N for No\n" % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
    else:
        return "The word doen`t exist."

word = input("Enter the word: ");

print(translate(word));
