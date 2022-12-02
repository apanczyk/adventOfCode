import fileinput

# X - rock, Y - paper, Z - scissors
results = {"X": ("Z", "Y", "X"),
           "Y": ("X", "Z", "Y"),
           "Z": ("Y", "X", "Z")}


def main():
    elves_list = load_game_list("file.txt")

    # 01
    counted_result = count_results(elves_list)
    print(counted_result)

    # 02
    elves_list = load_changed(elves_list)
    counted_result = count_results(elves_list)
    print(counted_result)


def load_game_list(file):
    game_list = []
    for line in fileinput.input(file):
        value = line.strip().split()
        value[0] = chr(ord(value[0]) + ord('X') - ord('A'))
        game_list.append(value)
    return game_list


def load_changed(elf_list: list):
    new_list = []
    for row in elf_list:
        new_list.append([row[0], change_data(row)])
    return new_list


def change_data(result):
    if result[1] == "X":
        return results[result[0]][0]
    elif result[1] == "Y":
        return results[result[0]][2]
    return results[result[0]][1]


def count_results(game_list: list):
    points = 0
    for result in game_list:
        if results.get(result[1])[0] == result[0]:
            points += 6
        if results.get(result[1])[2] == result[0]:
            points += 3
        points += ord(result[1]) % ord('W')
    return points


main()
