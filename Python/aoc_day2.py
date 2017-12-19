print("Advent Of Code - Day 2")

input = open('data_day2.txt', 'r').read()

checksum = 0

for line in input.split("\n"):
    row = list(map(int, line.split("\t")))
    checksum += max(row) - min(row)

print("Part 1, Checksum: " + str(checksum))