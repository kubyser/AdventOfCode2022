f = open("resources/day3_input.txt", "r")
lines = f.read().splitlines()
f.close()

sumP = 0

for l in lines:
    s1 = l[:int(len(l)/2)]
    s2 = l[int(len(l)/2):]
    for c in s1:
        if c in s2:
            sumP += ord(c) - ord('a') +1 if ord('a') <= ord(c) <= ord('z') else ord(c) - ord('A') + 27
            break

print("Part1: ", sumP)

sumP = 0
ln = 0
while ln < len(lines):
    for c in lines[ln]:
        if c in lines[ln+1] and c in lines[ln+2]:
            sumP += ord(c) - ord('a') +1 if ord('a') <= ord(c) <= ord('z') else ord(c) - ord('A') + 27
            break
    ln += 3

print("Part2: ", sumP)


