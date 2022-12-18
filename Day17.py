LEFT = "left"
RIGHT = "right"
DOWN = "down"
MINX = 1
MAXX = 7
MINY = 1
BIGNUM = 1000000000000
def checkCollision(cave, form, pos, direction):
    dX = -1 if direction == LEFT else 1 if direction == RIGHT else 0
    dY = -1 if direction == DOWN else 0
    for y in range(len(form)):
        for x in range(len(form[y])):
            if form[y][x] == '#':
                posCheck = (pos[0] + x + dX, pos[1] + y + dY)
                if posCheck[0] < MINX or posCheck[0] > MAXX or posCheck[1] < MINY or posCheck in cave:
                    return True
    return False


def printCave(cave, height):
    for y in range(height, 0, -1):
        s = "|"
        for x in range(7):
            s += "#" if (x+1, y) in cave else "."
        s += "|"
        print(s)
    print("+-------+")

f = open("resources/day17_input.txt", "r")
jets = f.read().splitlines()[0]
f.close()
forms = [["####"], [".#.", "###", ".#."], ["###", "..#", "..#"], ["#", "#", "#", "#"], ["##", "##"]]
cave = set()
height = 0
jetNum = 0
formNum = 0
stopAfterState = [-1, 0, 0] # forms, cur height, exp height
cache = {}
for i in range(1000000000000):
    if stopAfterState[0] == 0:
        expHeight = stopAfterState[2] + height - stopAfterState[1]
        print("Stop state reached! cur height", height, "Expected height:", expHeight)
        input("Press Enter to continue...")
    if stopAfterState[0] >= 0:
        stopAfterState[0] -= 1
    form = forms[formNum]
    formNum = formNum + 1 if formNum < len(forms)-1 else 0
    y = height + 4
    x = 3
    while True:
        jet = LEFT if jets[jetNum] == '<' else RIGHT
        jetNum = jetNum + 1 if jetNum < len(jets)-1 else 0
        if jetNum == 0:
            state = (formNum, x, y-height-4)
            if state not in cache:
                cache[state] = (i, height)
            else:
                prevState = cache[state]
                remaining = BIGNUM - i
                cycleLength = i - prevState[0]
                growth = height - prevState[1]
                cycles = int(remaining / cycleLength)
                mod = remaining % cycleLength
                expHeight = height + growth * cycles
                print("Fell:", i, "height:", height, "form: ", formNum, "pos:", x, y - height - 4)
                print("Cache hit!! cache fell:", prevState[0], "cache height:", prevState[1], "cycle=", cycleLength,
                      "growth:", growth, "remaining:", remaining, "cycle size=", cycleLength, "cycles left=", cycles, "mod: ", mod, "Expected height: ", expHeight)
                if stopAfterState[0] == -1:
                    stopAfterState = [mod-1, height, expHeight]
                # input("Press Enter to continue...")
                cache[state] = (i, height)
        if not checkCollision(cave, form, (x, y), jet):
            x = x-1 if jet == LEFT else x+1
        if not checkCollision(cave, form, (x, y), DOWN):
            y -= 1
        else:
            for fY in range(len(form)):
                for fX in range(len(form[fY])):
                    if form[fY][fX] == '#':
                        pos = (x + fX, y + fY)
                        cave.add(pos)
                        if pos[1] > height:
                            height = pos[1]
            break
    # print("==== CAVE AFTER ROCK", i+1, "====")
    # printCave(cave, height)
    # print("")
    # input("Press Enter to continue...")
print("Pile height:", height)
