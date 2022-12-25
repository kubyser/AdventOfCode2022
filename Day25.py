VALUE = {'1': 1, '2': 2, '0': 0, '-': -1, '=': -2}
SVALUE = {1: '1', 2: '2', 0: '0', -1: '-', -2: '='}

def snafuToDec(s):
    res = 0
    pow = 1
    for pos in range(len(s)-1, -1, -1):
        res += VALUE[s[pos]] * pow
        pow *= 5
    return res


def decToSnafy(d):
    carry = 0
    res = ""
    while d > 0:
        m = d % 5 + carry
        carry = 0
        if m > 2:
            m -= 5
            carry = 1
        res = SVALUE[m] + res
        d = int(d/5)
    if carry > 0:
        res = SVALUE[carry] + res
    return res



f = open("resources/day25_input.txt", "r")
lines = f.read().splitlines()
f.close()
sum = 0
for line in lines:
    res = snafuToDec(line)
    sum += res
    print(line, res, decToSnafy(res))
print("sum dec=", sum, "or in snafu:", decToSnafy(sum))