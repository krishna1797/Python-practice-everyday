import requests

word = input("Enter your word: ")

url =f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
lala = requests.get(url)
data =lala.json()

if isinstance(data, dict):
    print("Word not found!")
    exit()

meaning = data[0]["meanings"][0]
definition = meaning["definitions"][0]

part = meaning.get("partOfSpeech")
if part:
    print("Part of Speech:", part)
else:
    print("No part of speech found.")

definition_text = definition.get("definition")
if definition_text:
    print("Definition:", definition_text)
else:
    print("No definition found.")

synonyms = meaning.get("synonyms", [])
if synonyms:
    print("Synonyms:", ", ".join(synonyms))
else:
    print("No synonyms found.")

example = definition.get("example")
if example:
    print("Example:", example)
else:
    print("No example available.")

antonyms = definition.get("antonyms", [])
if antonyms:
    print("Antonyms:", ", ".join(antonyms))
else:
    print("No antonyms found.")