import sys
def gen_triplet():
    tripletlist = []
    count = int(sys.argv[1])
    limit = int(sys.argv[2])
    while len(tripletlist) < count:
        for i in range(1, limit):
            for j in range(i, limit):
                for k in range(j, limit):
                    if sum_triplet(i, j) == square_num(k):
                        tripletlist.append((i, j, k))

    return tripletlist

def sum_triplet(num1, num2):
    return num1 ** 3 + num2 ** 3

def square_num(num):
    return num ** 2

print(gen_triplet())

