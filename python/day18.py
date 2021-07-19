def read_data(fn):
    with open(fn, "r") as f:
        data = [l.strip() for l in f]
    return data


def parse_line_to_list(line):
    l_int = [int(c) for c in line if c not in ["+", "*", "(", ")"]]
    return l_int


def main():
    data = read_data("../data/day18.txt")
    single = data[0]
    parsed = parse_line_to_list(single)
    print(parsed)


if __name__ == "__main__":
    main()
