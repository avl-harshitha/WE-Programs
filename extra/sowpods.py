import sys


def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


word_dict = {}


def get_anag_list(word):
    anag_list = word_dict.get("".join(sorted(word)), [])
    return anag_list


def gen_anag_list(word_dict):
    return [wordlist for wordlist in word_dict.values() if len(wordlist) > 1]


def gen_word_dict(wordlist):
    for i in wordlist:
        anag_list = get_anag_list(i)
        anag_list.append(i)
        word_dict["".join(sorted(i))] = anag_list
    return word_dict


def parse_file(filename):
    words = []
    fp = open(filename, "r")
    for line in fp:
        words.append(line.strip("\n"))
    return words


def write_file(filename, anag_list):
    fp = open(filename, "w")
    for anag in anag_list:
        fp.write("%s\n" %anag)


def main(input_file, output_file):
    word_list = parse_file(input_file)
    word_dict = gen_word_dict(word_list)
    anag_list = gen_anag_list(word_dict)
    write_file(output_file, anag_list)


main(sys.argv[1], sys.argv[2])

