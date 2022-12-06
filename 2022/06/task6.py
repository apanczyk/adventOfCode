def main():
    code = load_code("file.txt")
    print(find_marker(code, 4))
    print(find_marker(code, 14))


def find_marker(code, distinct):
    for i in range(0, len(code)):
        if len(set(code[i:i + distinct])) == distinct:
            return i + distinct


def load_code(file):
    f = open(file, "r")
    return f.read()


main()
