# Process:
# - in first line, start at 0,0 check for tree
# - move to next line at appropriate position based on indices, check for tree
# - end when first index (vertical) is beyond length of top-level list

# - data should be list of list of chars


def read_data(fn, dx, dy):
    with open(fn, "r") as f:
        # Below we repeat the string to account for right movement
        # This is a hack
        # Should calculate how far right the pattern needs to go
        raw = [line.strip() for line in f]
        data = [line * 100 for line in raw]
    return data


def solve(data, x, y, dx, dy, trees):
    if y > (len(data) - 1):
        return trees
    else:
        if data[y][x] == "#":
            trees += 1
        print(x, y, trees)
        return solve(data, (x + dx), (y + dy), dx, dy, trees)


def partone():
    data = read_data("../data/day3.txt", 3, 1)
    answer = solve(data, 0, 0, 3, 1, 0)
    print(f"there are {answer} trees")


if __name__ == "__main__":
    partone()
