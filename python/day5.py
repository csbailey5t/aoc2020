def get_id(row, column):
    return (row * 8) + column


# Should abstract the search out of these get_* functions
def get_row(bpass):
    left = 0
    right = 127
    for l in bpass[:-3]:
        mid = (left + right) // 2
        if l == "F":
            right = mid
        else:
            left = mid + 1
    return left


def get_col(bpass):
    left = 0
    right = 7
    for l in bpass[-3:]:
        mid = (left + right) // 2
        if l == "L":
            right = mid
        else:
            left = mid + 1
    return left


def partone(fn):
    with open(fn, "r") as f:
        passes = [line.strip() for line in f]
    ids = [get_id(get_row(x), get_col(x)) for x in passes]
    return max(ids)


def parttwo(fn):
    with open(fn, "r") as f:
        passes = [line.strip() for line in f]
    sorted_ids = sorted([get_id(get_row(x), get_col(x)) for x in passes])
    for i in range(len(sorted_ids) - 1):
        if sorted_ids[i] + 2 == sorted_ids[i + 1]:
            return sorted_ids[i] + 1


if __name__ == "__main__":
    # answer = partone("../data/day5.txt")
    answer = parttwo("../data/day5.txt")
    print(answer)
