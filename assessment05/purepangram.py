from collections import Counter
import string

def calculate_index(count, char):
    index = 0
    vowelset = set("aeiou")
    if count > 1 and char in vowelset:
        index += 0.5
    elif count > 1 and char not in vowelset:
        index += 0.7
    if count == 3:
        index += 1
    elif count > 3:
        index += 3
    return index


def purityindexpangram(s):
    s = s.lower()
    s = s.replace(" ", "")
    countdict = Counter(s)
    index = 0
    for char in countdict.keys():
        count = countdict[char]
        index += calculate_index(count, char)
    return index

print(purityindexpangram("TV quiz drag nymphs blew JFK cox"))


