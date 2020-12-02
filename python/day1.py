from itertools import combinations

# Part 1


def get_product(data):
    combos = combinations(data, 2)
    for (x, y) in combos:
        if (x + y) == 2020:
            print(x * y)
            exit


def read_file_to_list(fn):
    with open(fn, "r") as f:
        data = set([int(ln.strip()) for ln in f.readlines() if ln != ""])
    return data


def partone():
    data = read_file_to_list("..data/day1.txt")
    get_product(data)


# Part 2
#
def get_product3(data):
    combos = combinations(data, 3)
    for (x, y, z) in combos:
        if (x + y + z) == 2020:
            print(x * y * z)
            exit


def parttwo():
    data = read_file_to_list("../data/day1.txt")
    get_product3(data)


if __name__ == "__main__":
    # partone()
    parttwo()
