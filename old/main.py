import fileinput

file_list = []

for line in fileinput.input("file.txt"):
    file_list.append(int(line.strip()))

measurements = 0
for element in range(3, len(file_list)):
    last = file_list[element - 3] + file_list[element - 2] + file_list[element - 1]
    current = file_list[element] + file_list[element - 1] + file_list[element - 2]
    if last < current:
        measurements += 1

print(measurements)
