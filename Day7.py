NAME = "NAME"
PARENT = "PARENT"
DIRS = "DIR"
FILES = "FILES"
SIZE = "SIZE"


def printDir(startDir, padding):
    for d in startDir[DIRS]:
        print(padding, "-", d, "(dir, size=", startDir[DIRS][d][SIZE], ")")
        printDir(startDir[DIRS][d], padding + "  ")
    for f in startDir[FILES]:
        print(padding, "-", f, "(file, size=", startDir[FILES][f], ")")


def printFilesystem(root):
    print ("- /")
    printDir(root, "  ")


def getDirsSmallerThan(root, maxSize):
    res = root[SIZE] if root[SIZE] <= maxSize else 0
    for d in root[DIRS]:
        res += getDirsSmallerThan(root[DIRS][d], maxSize)
    return res


def getDirClosestTo(root, targetSize):
    best = root
    for d in root[DIRS]:
        newBest = getDirClosestTo(root[DIRS][d], targetSize)
        if newBest:
            if newBest[SIZE] < best[SIZE]:
                best = newBest
    if best[SIZE] >= targetSize:
        return best
    else:
        return {}


f = open("resources/day7_input.txt", "r")
lines = f.read().splitlines()
f.close()
root = {DIRS: {}, FILES: {}, NAME: "/", SIZE: 0}
curDir = root
dirMode = False
for line in lines:
    #print("Line: ", line)
    com = line.split(" ")
    if com[0] == "$":
        dirMode = False
        if com[1] == "cd":
            if com[2] == "..":
                curDir = curDir[PARENT]
            elif com[2] == "/":
                curDir = root
            else:
                if com[2] in curDir[DIRS]:
                    curDir = curDir[DIRS][com[2]]
                else:
                    print("Unknown dir: ", line)
                    exit(-1)
            continue
        if com[1] == "ls":
            dirMode = True
            continue
        print("Unknown command: ", line)
        exit(-1)
    else:
        if not dirMode:
            print("Not command but not in dirMode: ", line)
            exit(-1)
        if com[0] == "dir":
            if com[1] not in curDir[DIRS]:
                newDir = {PARENT: curDir, DIRS: {}, FILES: {}, NAME: com[1], SIZE: 0}
                curDir[DIRS][com[1]] = newDir
            continue
        else:
            if com[1] not in curDir[FILES]:
                size = int(com[0])
                curDir[FILES][com[1]] = size
                pos = curDir
                while True:
                    pos[SIZE] += size
                    if PARENT in pos:
                        pos = pos[PARENT]
                    else:
                        break
printFilesystem(root)
print("Sum of dirs smaller than 100000: ", getDirsSmallerThan(root, 100000))
res = getDirClosestTo(root, 30000000 - 70000000 + root[SIZE])
print("Dir to delete:", res[NAME], "size=", res[SIZE])






