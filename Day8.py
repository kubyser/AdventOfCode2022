RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)
WIDTH = "width"
HEIGHT = "height"


def isVisible(map, startPos, direction):
    pos = startPos
    while True:
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        if pos[0] < 0 or pos[0] >= map[WIDTH] or pos[1] < 0 or pos[1] >= map[HEIGHT]:
            return True
        if map[pos] >= map[startPos]:
            return False


def getVisibleDistance(map, startPos, direction):
    pos = startPos
    dist = 0
    while True:
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        if pos[0] < 0 or pos[0] >= map[WIDTH] or pos[1] < 0 or pos[1] >= map[HEIGHT]:
            return dist
        dist += 1
        if map[pos] >= map[startPos]:
            return dist


f = open("resources/day8_input.txt", "r")
lines = f.read().splitlines()
f.close()
map = {HEIGHT: len(lines), WIDTH: len(lines[0])}
j = 0
for line in lines:
    i = 0
    for c in line:
        map[(i, j)] = int(c)
        i += 1
    j += 1
numVisible = 0
bestScore = 0
for j in range(map[HEIGHT]):
    for i in range(map[WIDTH]):
        pos = (i, j)
        if isVisible(map, pos, RIGHT) or isVisible(map, pos, LEFT) or \
                isVisible(map, pos, UP) or isVisible(map, pos, DOWN):
            numVisible += 1
        score = getVisibleDistance(map, pos, UP) * getVisibleDistance(map, pos, LEFT) * \
                getVisibleDistance(map, pos, DOWN) * getVisibleDistance(map, pos, RIGHT)
        if score > bestScore:
            bestScore = score
print("Visible trees:", numVisible)
print("Scenic score:", bestScore)
