print("Advent Of Code - Day 5")
PUZZLEINPUT = open('data_day5.txt', 'r').read()

# Part 1
memory = list(map(int, PUZZLEINPUT.split("\n")))

adress = 0
counter = 0

while adress < len(memory):
    next_adress = adress + memory[adress]
    memory[adress] = memory[adress] + 1
    adress = next_adress
    counter = counter + 1

print "Part 1, step count: " + str(counter)

memory = list(map(int, PUZZLEINPUT.split("\n")))

adress = 0
counter = 0
offset = 0

while adress < len(memory):

    next_adress = adress + memory[adress]
    if memory[adress] > 2:
        memory[adress] = memory[adress] - 1
    else:
        memory[adress] = memory[adress] + 1

    counter = counter + 1
    adress = next_adress

print "Part 2, step count: " + str(counter)
