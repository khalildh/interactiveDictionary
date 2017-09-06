from difflib import get_close_matches
import json

data = json.load(open("data.json"))

#print(data)



# def askForInput():
#     word = input("A word to define\n")
#     print(data[word])
#
# askForInput()


def translate(w):
    w = w.lower()
    matches = get_close_matches(w, data.keys(), 1)
    print(matches)
    if w in data:
        return data[w]
    elif len(matches) != 0:
        return matches[0]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translate(word))
