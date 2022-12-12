ITEMS = "items"
OPERATION = "operation"
TEST = "test"
IFTRUE = "iftrue"
IFFALSE = "iffalse"
VALUE = "value"
SVALUE = "svalue"
MOD = "mod"
PART1 = False
f = open("resources/day11_input.txt", "r")
lines = f.read().splitlines()
f.close()
monkeys = {}
liter = iter(lines)
tests = set()
while True:
    monkeyNum = int(next(liter).split()[1][:-1])
    sItemsStr = next(liter).split(":")[1]
    startItems = [{VALUE: int(x), SVALUE: int(x), MOD: {}} for x in sItemsStr.split(",")] if len(sItemsStr) > 0 else []
    op = next(liter).split(" = ")[1].split()
    test = int(next(liter).split(" by ")[1])
    if test not in tests:
        tests.add(test)
    ifTrue = int(next(liter).split("monkey ")[1])
    ifFalse = int(next(liter).split("monkey ")[1])
    monkeys[monkeyNum] = {ITEMS: startItems, OPERATION: op, TEST: test, IFTRUE: ifTrue, IFFALSE: ifFalse}
    try:
        line = next(liter)
    except StopIteration:
        break
for monkeyNum in range(len(monkeys)):
    m = monkeys[monkeyNum]
    for item in m[ITEMS]:
        for test in tests:
            item[MOD][test] = item[VALUE] % test
print(monkeys)
activity = [0] * len(monkeys)
for roundNum in range(20 if PART1 else 10000):
    #print("ROUND:", roundNum)
    for monkeyNum in range(len(monkeys)):
        #print(monkeys)
        m = monkeys[monkeyNum]
        for i in range(len(m[ITEMS])):
            wLevel = m[ITEMS][0][VALUE]
            sLevel = m[ITEMS][0][SVALUE]
            for test in tests:
                wMod = m[ITEMS][0][MOD][test]
                if m[OPERATION][1] == "*":
                    wMod = (wMod * wMod) % test if m[OPERATION][2] == "old" else (wMod * int(m[OPERATION][2])) % test
                elif m[OPERATION][1] == "+":
                    wMod = (wMod + int(m[OPERATION][2])) % test
                else:
                    print("ERROR: unrecognized operation:", m[OPERATION])
                    exit(-1)
                m[ITEMS][0][MOD][test] = wMod
            if PART1:
                if m[OPERATION][1] == "*":
                    wLevel = wLevel * wLevel if m[OPERATION][2] == "old" else wLevel * int(m[OPERATION][2])
                else:
                    wLevel += int(m[OPERATION][2])
                wLevel = int(wLevel / 3)
                m[ITEMS][0][VALUE] = wLevel
            testRes = wLevel % m[TEST] if PART1 else m[ITEMS][0][MOD][m[TEST]]
            # print("round:", roundNum, "sLevel:", sLevel, "monkey", monkeyNum, "wLevel:", wLevel,
            #      "op ", m[OPERATION][1:], "test", m[TEST], "res=", testRes)
            if testRes == 0:
                monkeys[m[IFTRUE]][ITEMS].append(m[ITEMS][0])
            else:
                monkeys[m[IFFALSE]][ITEMS].append(m[ITEMS][0])
            m[ITEMS] = m[ITEMS][1:]
            activity[monkeyNum] += 1
print(activity)
activity.sort(reverse=True)
print("Monkey business:", activity[0] * activity[1])
