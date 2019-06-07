import sys

def largest_str(str1, str2):
    return max(str1, str2, key=lambda x: len(x))


def smallest_str(str1, str2):
    return max(str1, str2, key=lambda x: -len(x))


def interweave_string():
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    large_str = largest_str(str1, str2)
    small_str = smallest_str(str1, str2)
    inter_string = "".join([str1[i] + str2[i] for i in range(len(small_str))])
    inter_string += large_str[len(small_str):]
    return inter_string


print(interweave_string())