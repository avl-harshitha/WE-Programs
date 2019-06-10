import sys

word_dict = {}


def extract_anag_list(word_dict):
    return [anaglist for anaglist in word_dict.values() if len(anaglist) > 1]


def build_anag_list(wordlist):
    for i in wordlist:
        word_dict["".join(sorted(i))] = word_dict.get("".join(sorted(i)), [])
        word_dict["".join(sorted(i))].append(i)
    return word_dict


def get_all_words(filename):
    return [line.strip("\n") for line in open(filename, "r")]


def print_anagrams(filename, anag_list):
    fp = open(filename, "w")
    for anag in anag_list:
        fp.write("%s\n" %anag)


def main(input_file, output_file):
    word_list = get_all_words(input_file)
    word_dict = build_anag_list(word_list)
    anag_list = extract_anag_list(word_dict)
    print_anagrams(output_file, anag_list)


main(sys.argv[1], sys.argv[2])

