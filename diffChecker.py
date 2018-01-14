from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a.lower().split(), b.lower().split()).ratio()

print(similar("My Name is James", "My name is James  "))
