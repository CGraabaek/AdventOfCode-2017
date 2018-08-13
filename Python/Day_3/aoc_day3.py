import ulamspiral

#S = ulamspiral.UlamSpiral(265150)
# S.show()

PUZZLEINPUT = int(open('input.txt', 'r').read())

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

# Coordinate for the number
X = 0
Y = 0

# Direction to start with
DIRECTION = 0
# Max step
MAX_STEPS = 1
# Step counter
STEPS_TAKEN = 0
# Direction change counters
DIRECTION_CHANGES = 0

for i in range(1, PUZZLEINPUT):
    # Going to the right
    if DIRECTION == EAST:
        X = X + 1
    # Going up
    if DIRECTION == NORTH:
        Y = Y + 1
    # Going left
    if DIRECTION == WEST:
        X = X - 1
    # Going down
    if DIRECTION == SOUTH:
        Y = Y - 1

    STEPS_TAKEN = STEPS_TAKEN + 1
    if STEPS_TAKEN == MAX_STEPS:
        DIRECTION_CHANGES = DIRECTION_CHANGES + 1
        DIRECTION = (DIRECTION + 1) % 4
        STEPS_TAKEN = 0
        if DIRECTION_CHANGES % 2 == 0:
            MAX_STEPS = MAX_STEPS + 1

print "Part 1: " + str(abs(X) + abs(Y))
