import fileinput


def main():
    code = load_list("file.txt")
    value = 0
    value_partial = 0
    for line in code:
        value += check_range(line)
        value_partial += check_range_2(line)
    print(value)
    print(value_partial)


def check_range(list_element: list):
    first = list(map(int, list_element[0].split('-')))
    second = list(map(int, list_element[1].split('-')))
    return (first[0] <= second[0] and first[1] >= second[1]) | \
           (second[0] <= first[0] and second[1] >= first[1])


def check_range_2(list_element: list):
    first = list(map(int, list_element[0].split('-')))
    second = list(map(int, list_element[1].split('-')))
    return (first[0] <= second[0] <= first[1]) | (second[0] <= first[0] <= second[1])


def load_list(file):
    str_list = []
    for line in fileinput.input(file):
        str_list.append(line.strip().split(','))
    return str_list


main()
