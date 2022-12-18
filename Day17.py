LEFT = "left"
RIGHT = "right"
DOWN = "down"
MINX = 1
MAXX = 7
MINY = 1
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
count = 0
mils = 0
for i in range(1000000000000):
    count = count + 1 if count < 9999 else 0
    if count == 0:
        mils += 1
        print("done", mils, "M, or ", mils/1000000000000*100, "%")
    form = forms[formNum]
    formNum = formNum + 1 if formNum < len(forms)-1 else 0
    y = height + 4
    x = 3
    while True:
        jet = LEFT if jets[jetNum] == '<' else RIGHT
        jetNum = jetNum + 1 if jetNum < len(jets)-1 else 0
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
