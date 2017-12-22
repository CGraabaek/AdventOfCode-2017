print "Advent Of Code - Day 2"

PUZZLEINPUT = open('data_day2.txt', 'r').read()

CHECKSUM = 0

for line in PUZZLEINPUT.split("\n"):
    row = list(map(int, line.split("\t")))
    CHECKSUM += max(row) - min(row)

print "Part 1, Checksum: " + str(CHECKSUM)


s = 0

for line in PUZZLEINPUT.split("\n"):
    row = list( map(int, line.split("\t")) )
    
    i = 0
    for i, a in enumerate(row):
        j = 0
        for j,b in enumerate(row):
            if i!=j and a%b==0:
                s += a/b

print "Part 2, Sum of the divided numbers " + str(s)