from collections import Counter
import string
import sys

def ispangram(s):
    s = s.lower()
    s = s.replace(" ", "")
    s = s.replace(".", "")
    countdict = (dict(Counter(s)))
    return set(string.ascii_lowercase) - set(countdict.keys()) == set()

print(ispangram(sys.argv[1]))


#return len(set(s)) == 26
