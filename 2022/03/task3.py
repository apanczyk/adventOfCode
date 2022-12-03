import fileinput


def main():
    string_list = load_string_list("file.txt")
    value_list = load_same_characters(string_list)
    print(sum(value_list))

    value_list_2 = load_same_characters_continued(string_list)
    print(sum(value_list_2))


def load_string_list(file):
    same_char_list = []
    for line in fileinput.input(file):
        same_char_list.append(line.strip())
    return same_char_list


def count_score(letter: str):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def load_same_characters_continued(string_list: list):
    same_char_count = []
    for i in range(2, len(string_list), 3):
        first = set(string_list[i - 2])
        second = set(string_list[i - 1])
        third = set(string_list[i - 0])
        same_char_count.append(count_score(list(first & second & third)[0]))
    return same_char_count


def load_same_characters(string_list: list):
    same_char_count = []
    for rucksack in string_list:
        first_half = set(rucksack[slice(0, len(rucksack) // 2)])
        second_half = set(rucksack[slice(len(rucksack) // 2, len(rucksack))])
        same_char_count.append(count_score(list(first_half & second_half)[0]))
    return same_char_count


main()
