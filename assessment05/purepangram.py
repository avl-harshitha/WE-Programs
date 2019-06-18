from collections import Counter
import string
import sys

def pick(count, char):
    vowelset = set("aeiou")
    if count > 1 and char in vowelset:
        return 1
    if count > 1 and char not in vowelset:
        return 2
    if count == 3:
        return 3
    if count > 3:
        return 4
    return 0


def calculate_index(count, char):
    impureindexlist = [0, 0.5, 0.7, 1, 3]
    return impureindexlist[pick(count, char)]


def purityindexpangram(s):
    s = s.lower()
    s = s.replace(" ", "")
    s = s.replace(".", "")
    if len(set(s)) == 26:
        return 0
    countdict = Counter(s)
    index = 0
    for char in countdict.keys():
        count = countdict[char]
        index += calculate_index(count, char)
    return index

print(purityindexpangram(sys.argv[1]))


