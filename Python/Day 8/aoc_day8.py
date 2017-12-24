from collections import defaultdict
import operator

print "Advent Of Code - Day 8"

PUZZLEINPUT = [x.split(" ") for x in open('input.txt', 'r').read().split("\n")]

def getCondition(c):
    if c==">":
        return operator.gt
    if c=="<":
        return operator.lt
    if c==">=":
        return operator.ge
    if c=="<=":
        return operator.le
    if c=="==":
        return operator.eq
    if c=="!=":
        return operator.ne

def testGetCondition(register1,condition,register2):
    if condition==">":
        return register1>register2
    if condition=="<":
        return register1<register2
    if condition==">=":
        return register1>=register2
    if condition=="<=":
        return register1<=register2
    if condition=="==":
        return register1==register2
    if condition=="!=":
        return register1!=register2

#regs = defaultdict(int)
regs = {}

for x in PUZZLEINPUT:
   # print testGetCondition(x[4],x[5],x[6])
    #Check if first register exists
    if x[0] not in regs:
        regs[x[0]] = 0
    #Check if second register exists
    if x[4] not in regs:
        regs[x[4]] = 0

    #Check the condition
    if testGetCondition(x[4],x[5],x[6]):
        if x[1] == 'inc':
            regs[x[0]] += int(x[2])
        if x[1] == 'dec':
            regs[x[0]] -= int(x[2])

print "Part 1, " + str(max(regs.values()))
