import functools
import sys


def inter_zip_string(str1, str2):
    fin_list = list(zip(str1, str2))
    fin_str = functools.reduce(lambda x, y: "".join(list(x) + list(y)), fin_list)
    min_len = min(len(str1), len(str2))
    fin_str += str1[min_len:] + str2[min_len:]
    return fin_str

print(inter_zip_string(sys.argv[1], sys.argv[2]))
