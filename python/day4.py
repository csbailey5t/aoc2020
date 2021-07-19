# Need all 8 fields, though cid is optional
import re


def validate_passport(passport):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    contained = [key for key in required_fields if key in passport]
    # print(contained)
    return True if (len(contained) == 7) else False


def partone(fn):
    with open(fn, "r") as f:
        raw = f.read()
    passports = raw.split("\n\n")
    valid_passports = list(filter(validate_passport, passports))
    print(len(valid_passports))


def validate_hgt(hgt):
    if hgt[-2:] in ["cm", "in"]:
        if (hgt[-2:] == "cm") & (int(hgt[:-2]) >= 150) & (int(hgt[:-2]) <= 193):
            return True
        if (hgt[-2:] == "in") & (int(hgt[:-2]) >= 59) & (int(hgt[:-2]) <= 76):
            return True
    return False


def validate_conditions(passport):
    # process to k:v pairs
    chunks = [pair.split(":") for pair in passport.split(" ")]
    fields = {vals[0]: vals[1] for vals in chunks}
    print(fields)
    # functions to check each condition
    attr_conditions = {
        "byr": lambda x: int(x) >= 1920 & int(x) <= 2002,
        "iyr": lambda x: int(x) >= 2010 & int(x) <= 2020,
        "eyr": lambda x: int(x) >= 2020 & int(x) <= 2030,
        "hgt": validate_hgt,
        "hcl": lambda x: re.match(r"^#[0-9a-f]{6}$", x) is not None,
        "ecl": lambda x: x in ["amb", "blue", "brn", "gry", "grn", "hzl", "oth"],
        "pid": lambda x: re.match(r"^[0-9]{9}$", x) is not None,
    }
    results = []
    for key, value in fields.items():
        if key in attr_conditions.keys():
            check = attr_conditions[key](value)
            results.append(check)
    print(set(results))
    return True if set(results) == {True} else False


def validate_passport_conditions(passport):
    # first check for necessary fields, then do further validation
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    # combine multiple lines of passport
    passport = passport.replace("\n", " ")
    if validate_passport(passport):
        conditions_pass = validate_conditions(passport)
        return conditions_pass
    else:
        return False


def parttwo(fn):
    with open(fn, "r") as f:
        raw = f.read()
    passports = raw.split("\n\n")
    valid_passports = list(filter(validate_passport_conditions, passports))
    print(len(valid_passports))


if __name__ == "__main__":
    # partone("../data/day4.txt")
    parttwo("../data/day4.txt")
