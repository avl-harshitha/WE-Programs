import itertools
import sys


def generate_readingslist(numofdigits):
    digitlist = [str(i) for i in range(1, 10)]
    return [int("".join(num)) for num in itertools.combinations(digitlist, numofdigits)]


def nextreading(presreading, readinglist):
    index = readinglist.index(presreading)
    return readinglist[(index + 1) % len(readinglist)]


def prevreading(presreading, readinglist):
    index = readinglist.index(presreading)
    return readinglist[(index - 1) % len(readinglist)]


def differencebwreading(firstreading, secondreading, readinglist):
    return readinglist.index(firstreading) - readinglist.find(secondreading)


def main(numofdigits):
    readinglist = generate_readingslist(numofdigits)
    print(nextreading(sys.argv[2], readinglist))
    print(prevreading(sys.argv[2], readinglist))
    print(differencebwreading(sys.argv[2], sys.argv[3], readinglist))

main(sys.argv[1])
