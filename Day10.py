f = open("resources/day10_input.txt", "r")
lines = f.read().splitlines()
f.close()
reg = 1
cycle = 0
strength = 0
crt = [""]
op = (False, 0)
reader = iter(lines)
while True:
    cycle += 1
    if not op[0]:
        try:
            line = next(reader)
        except StopIteration:
            break
    xpos = (cycle - 1) % 40
    print("Cycle", cycle, "x=", reg, "xpos=", xpos, "op=", op, "strength=", strength, "command=", line)
    crt[len(crt)-1] += "#" if xpos-1 <= reg <= xpos+1 else " "
    if (cycle - 20) % 40 == 0:
        strength += cycle * reg
    if op[0]:
        reg += op[1]
        op = (False, 0)
    else:
        s = line.split()
        if s[0] == "addx":
            op = (True, int(s[1]))
        else:
            op = (False, 0)
    if cycle % 40 == 0:
        crt.append("")
print("Sum of signal strengths:", strength)
for s in crt:
    print(s)
