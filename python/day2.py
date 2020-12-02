from collections import namedtuple


PasswordEntry = namedtuple("PasswordEntry", "min, max, letter, password")


def parse_line(line):
    chunks = line.split(":")
    password = chunks[1].strip()
    rule_chunk = chunks[0].split(" ")
    letter = rule_chunk[1]
    rules = rule_chunk[0].split("-")
    r1 = int(rules[0])
    r2 = int(rules[1])
    return PasswordEntry(r1, r2, letter, password)


def parse_passwords(fn):
    with open(fn, "r") as f:
        lines = f.readlines()
        pass_entries = [parse_line(line.strip()) for line in lines]
    return pass_entries


def check_valid_pass(pe):
    count = pe.password.count(pe.letter)
    return (count >= pe.min) & (count <= pe.max)


def part_one():
    pass_entries = parse_passwords("../data/day2.txt")
    valid_passwords = list(filter(check_valid_pass, pass_entries))
    print(len(valid_passwords))


def check_valid_passT(pe):
    return (
        (pe.password[pe.min - 1] == pe.letter) & (pe.password[pe.max - 1] != pe.letter)
    ) | (
        (pe.password[pe.min - 1] != pe.letter) & (pe.password[pe.max - 1] == pe.letter)
    )


def part_two():
    pass_entries = parse_passwords("../data/day2.txt")
    valid_passwords = list(filter(check_valid_passT, pass_entries))
    print(len(valid_passwords))


if __name__ == "__main__":
    # part_one()
    part_two()
