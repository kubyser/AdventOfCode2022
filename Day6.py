f = open("resources/day6_input.txt", "r")
line = f.read().splitlines()[0]
f.close()
numChars = 14
pos = numChars
while True:
    subset = line[pos-numChars: pos]
#    print(subset)
    dist = set(subset)
#    print(dist)
    if (len(dist)) == numChars:
        print("Answer for size ", numChars, ": ", pos)
        break
    pos += 1


