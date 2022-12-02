import fileinput

# X - rock, Y - paper, Z - scissors
results = {"X": ("Z", "Y", "X"),
           "Y": ("X", "Z", "Y"),
           "Z": ("Y", "X", "Z")}


def main():
    elves_list = load_elves_list("file.txt")
    elves_list = load_changed(elves_list)
    top_3_elves = count_results(elves_list)
    print(top_3_elves)


def load_elves_list(file):
    elves_list = []
    for line in fileinput.input(file):
        value = line.strip().split()
        value[0] = chr(ord(value[0]) + ord('X') - ord('A'))
        elves_list.append(value)
    return elves_list


def load_changed(elf_list: list):
    new_list = []
    for row in elf_list:
        new_list.append([row[0], change_data(row)])
    return new_list


def change_data(result):
    if result[1] == "X":
        return results[result[0]][1]
    if result[1] == "Y":
        return results[result[0]][2]
    if result[1] == "Z":
        return results[result[0]][0]


def count_results(elf_list: list):
    ally = 0
    opponent = 0
    for result in elf_list:
        xd = results.get(result[1])
        if xd[0] == result[0]:
            opponent += 6
        if xd[1] == result[0]:
            ally += 6
        if xd[2] == result[0]:
            ally += 3
            opponent += 3
        opponent += ord(result[1]) % ord('W')
        ally += ord(result[0]) % ord('W')

    return [opponent, ally]


main()
