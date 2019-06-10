import sys
from collections import Counter

def get_all_words(filename):
    wordlist = [word for line in open(filename, "r") for word in line.strip("\n").split(" ")]
    return wordlist

def getfreqofwords(wordlist):
    return Counter(wordlist)

def getmaxfreqwords(maxnum, freqdict):
    return freqdict.most_common(maxnum)


def main(filename, maxnum):
    wordlist = get_all_words(filename)
    freqdict = getfreqofwords(wordlist)
    return getmaxfreqwords(maxnum, freqdict)


print(main(sys.argv[1], sys.argv[2]))

