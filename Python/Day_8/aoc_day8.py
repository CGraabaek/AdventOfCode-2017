import operator

print "Advent Of Code - Day 8"

PUZZLEINPUT = [x.split(" ") for x in open('input.txt', 'r').read().split("\n")]

def evaluateCondition(register1, condition, register2):
    if condition == ">":
        return REGS[register1] > int(register2)
    if condition == "<":
        return REGS[register1] < int(register2)
    if condition == ">=":
        return REGS[register1] >= int(register2)
    if condition == "<=":
        return REGS[register1] <= int(register2)
    if condition == "==":
        return REGS[register1] == int(register2)
    if condition == "!=":
        return REGS[register1] != int(register2)


# Create key/value pair (dictionary)
REGS = {}
MAX_VALUES = []

for x in PUZZLEINPUT:
    # Check if first register exists
    if x[4] not in REGS:
        REGS[x[4]] = 0
       
    # Check if second register exists
    if x[0] not in REGS:
        REGS[x[0]] = 0

    # Check the condition
    if evaluateCondition(x[4], x[5], x[6]):
        if x[1] == 'inc':
            REGS[x[0]] += int(x[2])
        if x[1] == 'dec':
            REGS[x[0]] -= int(x[2])
        MAX_VALUES.append(REGS[x[0]])

# Take highest value of the key/value pair.
print "Part 1, " + str(max(REGS.values()))
print "Part 2,  " + str(max(MAX_VALUES))
