print("Advent Of Code - Day 3")

inp = [i.strip().split() for i in open('data_day3.txt', 'r').readlines()]

passphrases = []

p1 = 0
p2 = 0

for i in inp:
    if len(set(i)) == len(i):
        p1 += 1
    # if len(set(''.join(sorted(u)) for u in i)) == len(i):
    if (sorted(''.join(sorted(set(i))) ) == len(i)):
        p2 += 1

#s = set()
#any(x in s or s.add(x) for x in passphrases)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))







