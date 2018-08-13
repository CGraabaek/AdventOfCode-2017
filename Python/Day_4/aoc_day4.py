print "Advent Of Code - Day 4"

PUZZLEINPUT = [i.strip().split() for i in open('input.txt', 'r').readlines()]

P1 = 0
P2 = 0

for words in PUZZLEINPUT:

    # If the length of the word
    if len(set(words)) == len(words):
        P1 += 1
    #Create array with all the words, where each word has been sorted
    words = [''.join(sorted(x)) for x in words]
    # i
    if len(words) == len(set(words)):
        P2 += 1

print "Part 1: " + str(P1)
print "Part 2: " + str(P2)
