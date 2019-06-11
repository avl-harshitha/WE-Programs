
import sys
import itertools


def rle(inputstr):
    contseqlist = [(char, len(list(seq))) for (char, seq) in itertools.groupby(inputstr)]
    for seq in contseqlist:
        if seq[1] > 2:
            inputstr = inputstr.replace(seq[0] * seq[1], str(seq[1]) + seq[0])
    return inputstr


def irle(inputrevstr):
    origstr = []
    for i in range(len(inputrevstr)):
        if inputrevstr[i].isdigit():
            origstr.append(int(inputrevstr[i]) * inputrevstr[i + 1])
        else:
            origstr.append(inputrevstr[i])
    return "".join(origstr)


def main():
    replacestr = rle(sys.argv[1])
    print(replacestr)
    print(irle(replacestr))


main()



