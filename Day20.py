data = []
realData = []


def printData(prefix=""):
    global data
    s = sorted(data, key=lambda x : x[1])
    a = [x[0] for x in s]
    print(prefix, a)


def printRealData(prefix=""):
    global realData
    a = [x[0] for x in realData]
    print(prefix, a)

def shift(dataPos, dir, debug=False):
    global data
    oldPos = data[dataPos][1]
    newPos = (oldPos + dir % (len(data)-1)) % len(data)
    if dir < 0:
        newPos = newPos+1 if newPos < len(data)-1 else 0
    if debug:
        print("Moving", data[dataPos][0], "from", oldPos, "to", newPos)
    for pos in range(len(data)):
        posCheck = data[pos][1]
        if dir > 0 and (newPos > oldPos and oldPos < posCheck <= newPos or \
                (newPos < oldPos and (posCheck > oldPos or posCheck <= newPos))):
            posUpdate = posCheck-1 if posCheck > 0 else len(data)-1
            data[pos][1] = posUpdate
        elif dir < 0 and (newPos < oldPos and newPos <= posCheck < oldPos or \
                (newPos > oldPos and (posCheck < oldPos or posCheck >= newPos))):
            posUpdate = posCheck+1 if posCheck < len(data)-1 else 0
            data[pos][1] = posUpdate
    data[dataPos][1] = newPos


def shiftByValue(value, dir):
    global data
    dPos = [i for i in range(len(data)) if data[i][0] == value][0]
    shift(dPos, dir)


def readData(lines):
    global data
    global realData
    pos = 0
    data = []
    realData = []
    for s in lines:
        data.append([int(s), pos])
        realData.append([int(s), pos])
        pos += 1


def simulate(dataPos, dir):
    global data
    global realData
    pos = [i for i in range(len(realData)) if realData[i][1] == dataPos][0]
    d = 1 if dir > 0 else -1
    for i in range(abs(dir)):
        newPos = pos+d
        if newPos == -1:
            newPos = len(realData)-1
        elif newPos == len(realData):
            newPos = 0
        v = realData[pos]
        realData[pos] = realData[newPos]
        realData[newPos] = v
        pos = newPos


def areEqual():
    global data
    s = sorted(data, key=lambda x : x[1])
    a = [x[0] for x in s]
    b = [x[0] for x in realData]
    pos1 = a.index(0)
    pos2 = b.index(0)
    for i in range(len(data)):
        if a[pos1] != b[pos2]:
            return False
        pos1 = pos1+1 if pos1 < len(a)-1 else 0
        pos2 = pos2+1 if pos2 < len(b)-1 else 0
    return True


f = open("resources/day20_input.txt", "r")
lines = f.read().splitlines()
f.close()
readData(lines)
if False:
    printData()
    for i in range(30):
        readData(lines)
        shift(2, -i, debug=True)
        printData("shifted first element by " + str(i))
    exit(-1)
part2 = True
if part2:
    for d in data:
        d[0] *= 811589153
for iter in range(10 if part2 else 1):
    print("Start iteration", iter)
    for d in range(len(data)):
        value = data[d][0]
        # print("moving", data[d])
        shift(d, value, debug=False)
        #simulate(d, value)
        #printData()
        #print("vvvvvv Sim")
        #printRealData()
        #print("^^^^^^ Sim")
        #if not areEqual():
        #    print("Not equal at", d, data[d])
        #    exit(-1)
    #    printData()
zeroPos = data[[i for i in range(len(data)) if data[i][0] == 0][0]][1]
print("Zeropos:", zeroPos)
interestingPos = [(x + zeroPos) % len(data) for x in [1000, 2000, 3000]]
print("Interesting pos:", interestingPos)
resValues = [x[0] for x in data if x[1] in interestingPos]
print("Res values:", resValues)
res = sum(resValues)
print("Decoded sum:", res)




