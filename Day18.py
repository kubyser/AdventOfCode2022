f = open("resources/day18_input.txt", "r")
lines = f.read().splitlines()
f.close()
lava = {}
minPos = [int(x) for x in lines[0].split(",")]
maxPos = [int(x) for x in lines[0].split(",")]
dc = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]
for line in lines:
    pos = [int(x) for x in line.split(",")]
    lava[(pos[0], pos[1], pos[2])] = 6
    if pos[0] < minPos[0]:
        minPos[0] = pos[0]
    if pos[1] < minPos[1]:
        minPos[1] = pos[1]
    if pos[2] < minPos[2]:
        minPos[2] = pos[2]
    if pos[0] > maxPos[0]:
        maxPos[0] = pos[0]
    if pos[1] > maxPos[1]:
        maxPos[1] = pos[1]
    if pos[2] > maxPos[2]:
        maxPos[2] = pos[2]
total = 0
for d in lava:
    count = lava[d]
    for diff in dc:
        if (d[0]+diff[0], d[1]+diff[1], d[2]+diff[2]) in lava:
            count -= 1
    lava[d] = count
    total += count
print("Total sides:", total)
