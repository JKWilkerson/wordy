import json

#   Setting variable `data` as type dict
data = json.load(open("data.json"))

def finder(word: str):
    """Searches the data file for a given word and prints its definitions."""
#   word = input("Please enter a search term: ")
#   @@@ Flesh out this docstring when/as needed.
    if word in data:
        for i in data[word]:
            print(i)

finder("rain")
