ITEMS = "items"
OPERATION = "operation"
TEST = "test"
IFTRUE = "iftrue"
IFFALSE = "iffalse"
PART1 = False
f = open("resources/day11_test_input.txt", "r")
lines = f.read().splitlines()
f.close()
monkeys = {}
liter = iter(lines)
while True:
    monkeyNum = int(next(liter).split()[1][:-1])
    startItems = [(int(x),int(x)) for x in next(liter).split(": ")[1].split(",")]
    op = next(liter).split(" = ")[1].split()
    test = int(next(liter).split(" by ")[1])
    ifTrue = int(next(liter).split("monkey ")[1])
    ifFalse = int(next(liter).split("monkey ")[1])
    monkeys[monkeyNum] = {ITEMS: startItems, OPERATION: op, TEST: test, IFTRUE: ifTrue, IFFALSE: ifFalse}
    try:
        line = next(liter)
    except StopIteration:
        break
print(monkeys)
activity = [0] * len(monkeys)
for roundNum in range(20 if PART1 else 20):
    #print("ROUND:", roundNum)
    for monkeyNum in range(len(monkeys)):
        #print(monkeys)
        m = monkeys[monkeyNum]
        for i in range(len(m[ITEMS])):
            wLevel = m[ITEMS][0][0]
            sLevel = m[ITEMS][0][1]
            if monkeyNum == 2:
                print("sLevel:", sLevel, "monkey", monkeyNum, "level", wLevel)
            value = wLevel if m[OPERATION][2] == "old" else int(m[OPERATION][2])
            if m[OPERATION][1] == "*":
                wLevel *= value
            elif m[OPERATION][1] == "+":
                wLevel += value
            else:
                print("ERROR: unrecognized operation:", m[OPERATION])
                exit(-1)
            if PART1:
                wLevel = int(wLevel / 3)
            if wLevel % m[TEST] == 0:
                monkeys[m[IFTRUE]][ITEMS].append((wLevel, sLevel))
            else:
                monkeys[m[IFFALSE]][ITEMS].append((wLevel, sLevel))
            m[ITEMS] = m[ITEMS][1:]
            activity[monkeyNum] += 1
print(activity)
activity.sort(reverse=True)
print("Monkey business:", activity[0] * activity[1])
