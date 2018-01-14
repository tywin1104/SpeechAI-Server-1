from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a.lower().split(), b.lower().split()).ratio()

