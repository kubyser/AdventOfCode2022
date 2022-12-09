f = open("resources/day1_input.txt", "r")
lines = f.read().splitlines()
f.close()
maxCals = []
cal = 0
for line in lines:
    if line == "":
        maxCals.append(cal)
        cal = 0
    else:
        cal += int(line)
maxCals.append(cal)
maxCals.sort(reverse=True)
print("Maximum calories:", maxCals[0])
print("Maximum 3 elfs' calories:", maxCals[0] + maxCals[1] + maxCals[2])