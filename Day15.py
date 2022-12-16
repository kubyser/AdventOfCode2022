def getManhattanDistance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def getIntersection(sensor, dist, y):
    minX = sensor[0] - (dist - abs(sensor[1] - y))
    maxX = sensor[0] + (dist - abs(sensor[1] - y))
    return minX, maxX


f = open("resources/day15_input.txt", "r")
lineY = 2000000
searchArea = 4000000
# lineY = 10
# searchArea = 20
lines = f.read().splitlines()
f.close()
beacons = set()
sensors = {}
for line in lines:
    s = line.split()
    sx = int(s[2].split(',')[0].split('=')[1])
    sy = int(s[3].split(':')[0].split('=')[1])
    bx = int(s[8].split(',')[0].split('=')[1])
    by = int(s[9].split('=')[1])
    dist = getManhattanDistance((sx, sy), (bx, by))
    sensors[(sx, sy)] = dist
    beacons.add((bx, by))
beaconFree = set()
for s in sensors:
    dist = sensors[s]
    if abs(s[1] - lineY) > dist:
        continue
    minX, maxX = getIntersection(s, sensors[s], lineY)
    for x in range(minX, maxX+1):
        if (x, lineY) not in beacons and x not in beaconFree:
            beaconFree.add(x)
print("Beaconless positions in line", lineY, ":", len(beaconFree))
found = False
for y in range(searchArea+1):
    if found:
        break
    beaconFree = []
    noFreePlaces = False
    for s in sensors:
        dist = sensors[s]
        if abs(s[1] - y) > dist:
            continue
        minX, maxX = getIntersection(s, sensors[s], y)
        minX = max(minX, 0)
        maxX = min(maxX, searchArea+1)
        consumed = False
        for p in beaconFree:
            if minX > p[1] or maxX < p[0]:
                continue
            consumed = True
            if minX >= p[0] and maxX <= p[1]:
                break
            if minX <= p[0]:
                p[0] = minX
            else:
                minX = p[0]
            if maxX >= p[1]:
                p[1] = maxX
            else:
                maxX = p[1]
        if not consumed:
            beaconFree.append([minX, maxX])
        for p in beaconFree:
            if p[0] == 0 and p[1] == searchArea+1:
                noFreePlaces = True
                break
        if noFreePlaces:
            break
    if noFreePlaces:
        # if y % 10000 == 0:
        #    print("line ", y)
        continue
    else:
        found = True
        print("======== FREE IN LINE: ", y)
        for x in range(searchArea+1):
            free = False
            for bf in beaconFree:
                if bf[0] <= x <= bf[1]:
                    free = True
                    break
            if not free:
                print("Coords:", x, y, "Tuning frequency:", x * 4000000 + y)
                break
        break
print("Finished")
