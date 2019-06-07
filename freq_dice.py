
import random
import sys


def throw_dice(numofdice=2):
    return random.randrange(1, 6 * numofdice + 1)


def gen_freq_dict():
    freq_dict = dict(zip(range(1, 13), [0] * 12))
    return freq_dict


def gen_freq_table(count=10000):
    freq_dict = gen_freq_dict()
    for i in range(count):
        freq_dict[throw_dice()] += 1
    return freq_dict


def compare_table():
    freq_count = int(sys.argv[1])
    numofdice = int(sys.argv[2])
    freq_table = gen_freq_table(freq_count)
    expect_val = freq_count // (numofdice * 6)
    compar_val = tuple(zip(freq_table.values(), [expect_val] * 12))
    return compar_val

print(compare_table())


