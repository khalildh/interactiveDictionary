from difflib import get_close_matches
import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys(), 1)) > 0:
        yn =input("Did you mean {} instead? Enter Y if yes, or N if no.".format(get_close_matches(w, data.keys(), 1)[0]))
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys(), 1)[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."

    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
