part1 = False

f = open("resources/day5_input.txt", "r")
lines = f.read().splitlines()
f.close()

piles = {}
ln = 0
while True:
    l = lines[ln]
    if l[1] == "1":
        break
    pos = 0
    while pos*4 < len(l):
        if pos+1 not in piles:
            piles[pos+1] = []
        if l[pos*4] == "[":
            piles[pos+1] = [l[pos*4 + 1]] + piles[pos+1]
        pos += 1
    ln += 1
print(piles)
for l in lines[ln+2:]:
    l = l[5:]
    ls = l.split(" from ")
    num = int(ls[0])
    fromPile = int(ls[1].split(" to ")[0])
    toPile = int(ls[1].split(" to ")[1])
    print(num, fromPile, toPile)
    if part1:
        for pos in range(num):
            piles[toPile].append(piles[fromPile][len(piles[fromPile]) - pos - 1])
    else:
        piles[toPile] += piles[fromPile][-num:]
    piles[fromPile] = piles[fromPile][: -num]
    print(piles)
final = ""
for pile in piles.values():
    if len(pile) > 0:
        final += pile[len(pile)-1]
print("Part1: ", final)

