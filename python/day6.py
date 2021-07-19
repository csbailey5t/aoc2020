from functools import reduce


def get_groups(lst):
    return [l.strip() for l in lst.split("\n\n")]


def clean_questions(group):
    return group.replace("\n", "").strip()


def partone(fn):
    with open(fn, "r") as f:
        data = f.read()
    groups = get_groups(data)
    q = [clean_questions(group) for group in groups]
    numq = [len(set(group)) for group in q]
    total = sum(numq)
    print(total)


def get_persons(group):
    return group.split("\n")


def get_common(persons):
    """
    Takes a list of persons (a group) and returns questions (chars) common to all
    Each person is represented as a string
    """
    return len(set.intersection(*[set(person) for person in persons]))


def parttwo(fn):
    with open(fn, "r") as f:
        data = f.read()
    groups = get_groups(data)
    group_persons = [get_persons(group) for group in groups]
    numc = [get_common(group) for group in group_persons]
    total = sum(numc)
    print(total)


if __name__ == "__main__":
    parttwo("../data/day6.txt")
