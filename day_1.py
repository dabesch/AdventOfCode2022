def read_data(file_path):
    # May have over-engineered this, was expecting the worst!
    cal_data = open(file_path).read()

    output_data = {}
    id_ = 1
    sub_list = []
    for line in cal_data.splitlines():
        if line == '':
            output_data[id_] = sum(sub_list)
            sub_list = []
            id_ += 1
        else:
            sub_list.append(int(line))
    return output_data


def top_x(data, x):
    cal_list = list(data.values())
    cal_list.sort(reverse=True)
    return cal_list[:x]


if __name__ == '__main__':
    data_path = './data/day_1.txt'
    elf_data = read_data(data_path)

    # Part 1
    print(top_x(elf_data, 1))
    # Part 2
    print(sum(top_x(elf_data, 3)))
