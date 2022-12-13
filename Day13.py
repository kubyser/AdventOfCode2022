TYPE = "type"
INT = "int"
VALUE = "value"
LIST = "list"
LESS = "less"
MORE = "more"
TIE = "tie"
def compare(a, b):
    if a[TYPE] == INT and b[TYPE] == INT:
        return LESS if a[VALUE] < b[VALUE] else MORE if a[VALUE] > b[VALUE] else TIE
    if a[TYPE] == LIST and b[TYPE] == LIST:
        for i in range(len(a[VALUE])):
            if i >= len(b[VALUE]):
                return MORE
            res = compare(a[VALUE][i], b[VALUE][i])
            if res != TIE:
                return res
        return LESS if len(a[VALUE]) < len(b[VALUE]) else TIE
    if a[TYPE] == INT:
        newA = {TYPE: LIST, VALUE: [{TYPE: INT, VALUE: a[VALUE]}]}
        return compare(newA, b)
    newB = {TYPE: LIST, VALUE: [{TYPE: INT, VALUE: b[VALUE]}]}
    return compare(a, newB)


def parse(line, pos):
    if line[pos] == '[':
        if line[pos+1] == ']':
            return {TYPE: LIST, VALUE: []}, pos + 2
        res = []
        curPos = pos
        while True:
            curPos += 1
            item = parse(line, curPos)
            res.append(item[0])
            curPos = item[1]
            if line[curPos] == ']':
                return {TYPE: LIST, VALUE: res}, curPos + 1
            if line[curPos] != ',':
                print("Unexpected symbol", line[curPos], " in ", line, "at pos", curPos)
                exit(-1)
    curPos = pos
    s = ""
    while True:
        s += line[curPos]
        curPos += 1
        if curPos >= len(line) or line[curPos] in {',', ']'}:
            return {TYPE: INT, VALUE: int(s)}, curPos


def countSmaller(packets, item):
    res = 0
    for i in range(len(packets)):
        if compare(item, packets[i]) == MORE:
            res += 1
    return res


f = open("resources/day13_input.txt", "r")
lines = f.read().splitlines()
f.close()
liter = iter(lines)
num = 1
sumCorrect = 0
packets = []
while True:
    lineA = next(liter)
    lineB = next(liter)
    a = parse(lineA, 0)[0]
    b = parse(lineB, 0)[0]
    packets.append(a)
    packets.append(b)
    res = compare(a, b)
    print(lineA, "to", lineB, ":", res)
    if res == LESS:
        sumCorrect += num
    try:
        next(liter)
    except StopIteration:
        break
    num += 1
print("Sum of correct indices:", sumCorrect)
divider1 = parse('[[2]]', 0)[0]
divider2 = parse('[[6]]', 0)[0]
decKey = (countSmaller(packets, divider1) + 1) * (countSmaller(packets, divider2) + 2)
print("Decoder key:", decKey)
