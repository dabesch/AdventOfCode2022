def find_important(c1, c2):
    set_1 = set([c for c in c1])
    set_2 = set([c for c in c2])
    return list(set_1.intersection(set_2))[0]


def get_group_important(r1, r2, r3):
    # I'm sure I should have done this smarter...
    r1 = set([i for i in r1])
    r2 = set([i for i in r2])
    r3 = set([i for i in r3])
    return list(r1.intersection(r2).intersection(r3))[0]


def get_value(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


def priority_scores(rucksack_data):
    priority_sum = 0
    for r in rucksack_data:
        split_val = int(len(r) / 2)
        comp1 = r[:split_val]
        comp2 = r[split_val:]
        imp = find_important(comp1, comp2)
        priority_sum += get_value(imp)
    return priority_sum


def group_scores(rucksack_data):
    groups = [i for i in range(3, len(rucksack_data) + 3, 3)]
    score = 0
    for g in groups:
        group_rucksacks = rucksack_data[g - 3:g]
        imp = get_group_important(*group_rucksacks)
        score += get_value(imp)
    return score


if __name__ == '__main__':
    data = open('data/day_3.txt').read()
    rucksacks = [i for i in data.split()]

    # Part 1
    print(priority_scores(rucksacks))

    # Part 2
    print(group_scores(rucksacks))
