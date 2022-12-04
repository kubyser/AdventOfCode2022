def contains(l1, l2):
    return True if l1[0] <= l2[0] and l1[1] >= l2[1] else False


def overlaps(l1, l2):
    return True if l1[0] <= l2[0] <= l1[1] or l1[0] <= l2[1] <= l1[1] or l2[0] <= l1[0] and l2[1] >= l1[1] else False


f = open("resources/day4_input.txt", "r")
lines = f.read().splitlines()
f.close()
numContainted = 0
numOverlapping = 0
for l in lines:
    s = l.split(",")
    for i in range(len(s)):
        s[i] = list(map(int, s[i].split("-")))
    if contains(s[0], s[1]) or contains(s[1], s[0]):
        numContainted += 1
    if overlaps(s[0], s[1]):
        numOverlapping += 1
print("Part1: ", numContainted)
print("Part2: ", numOverlapping)
