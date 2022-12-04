def create_range(string):
    start, finish = string.split('-')
    array = range(int(start), int(finish) + 1)
    return [a for a in array]


def check_overlap(array_1, array_2):
    res = 0
    if min(array_1) in array_2 and max(array_1) in array_2:
        res = 1
    elif min(array_2) in array_1 and max(array_2) in array_1:
        res = 1
    return res


def part_2_overlaps(array_1, array_2):
    set_1 = set(array_1)
    set_2 = set(array_2)
    inter = len(set_1.intersection(set_2))
    return int(inter > 0)


if __name__ == '__main__':
    data = open('data/day_4.txt').readlines()
    pairs = [d.strip().split(',') for d in data]

    overlaps = 0
    p2_overlaps = 0
    for p in pairs:
        a1 = create_range(p[0])
        a2 = create_range(p[1])
        overlaps += check_overlap(a1, a2)
        p2_overlaps += int(part_2_overlaps(a1, a2))

    # Part 1
    print(overlaps)
    # Part 2
    print(p2_overlaps)
