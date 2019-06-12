import itertools
import sys


def inter_zip_string(str1, str2):
    return "".join(["".join(pair) for pair in list(itertools.zip_longest(str1, str2, fillvalue=""))])


print(inter_zip_string(sys.argv[1], sys.argv[2]))
