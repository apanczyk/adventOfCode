import fileinput


def main():
    elves_list = load_elves_list("file.txt")
    top_elf = max(elves_list)
    top_3_elves = find_top_n_elves(sorted(elves_list), 3)
    print(top_elf)
    print(top_3_elves)


def load_elves_list(file):
    elves_list = [0]
    for line in fileinput.input(file):
        try:
            elves_list[len(elves_list)-1] += int(line.strip())
        except Exception:
            elves_list.append(0)
    return elves_list


def find_top_n_elves(elf_list, count, elf_sum=0):
    for _ in range(0, count):
        elf_sum += elf_list.pop()
    return elf_sum


main()
