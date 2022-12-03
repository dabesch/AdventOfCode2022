def translate(x):
    ref = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    return ref[x]


def score_round(p1, p2):
    sub_score = 0
    score_array = score_dict[p1]
    if p2 == p1:
        sub_score += 3
    elif p2 == score_array[0]:
        sub_score += 6
    sub_score += score_array[1]
    return sub_score


def get_values(x, plan):
    # return the value needed to match the plan
    if plan == 'win':
        value = op_dict[x]
    elif plan == 'draw':
        value = x
    else:
        value = score_dict[x][0]
    return value


if __name__ == '__main__':

    data = open('data/day_2.txt').read().strip()
    strategy = [i.split() for i in data.split('\n')]
    score_dict = {
        'A': ['C', 1],  # rock
        'B': ['A', 2],  # paper
        'C': ['B', 3]   # scissors
    }
    op_dict = {v[0]: k for k, v in score_dict.items()}

    result_dict = {
        'X': 'lose', 'Y': 'draw', 'Z': 'win'
    }

    # Part 1
    score_1 = 0
    for p2, p1 in strategy:
        p1 = translate(p1)
        score_1 += score_round(p1, p2)
    print(score_1)

    # Part 2
    score_2 = 0
    for p2, res in strategy:
        plan = result_dict[res]
        val = get_values(p2, plan)
        score_2 += score_dict[val][1]
        if plan == 'win':
            score_2 += 6
        elif plan == 'draw':
            score_2 += 3

    print(score_2)
