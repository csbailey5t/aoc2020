import re


def read_data(fn):
    with open(fn, "r") as f:
        data = [l.strip() for l in f]
    return data


def add_numbers(line):
    numb = 0
    clean_match = line.replace("(", "").replace(")", "").replace(" ", "")
    matches = re.finditer(r"\d*[\+\*]\d*", clean_match, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        if matchNum == 1:
            numb = eval(match.group())
        else:
            numb = eval("{}{}".format(numb, match.group()))
    return numb


def regex_match(line):
    regex = r"\([\d\s\+\*]+\)"
    r1 = re.findall(regex, line)
    # 5 * 9 * (7 * 3 * 3 + 9 * 3 + 56)
    for match in r1:
        numb = add_numbers(match)
        line = line.replace(match, str(numb))
    return line


def main():
    # data = read_data("test.txt")
    data = read_data("../data/day18.txt")
    total = 0
    for line in data:
        line = regex_match(line)
        while "(" in line:
            line = regex_match(line)
        total += int(add_numbers(line))
    print(total)

    # print(data[:5])


if __name__ == "__main__":
    main()
