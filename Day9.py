f = open("resources/day9_input.txt", "r")
lines = f.read().splitlines()
f.close()
ROPELENGTH = 10
rope = [(0, 0)] * ROPELENGTH
visited = {rope[ROPELENGTH - 1]}
for line in lines:
    dir = line.split(" ")[0]
    dist = int(line.split(" ")[1])
    xSpeed = 1 if dir == "R" else -1 if dir == "L" else 0
    ySpeed = 1 if dir == "U" else -1 if dir == "D" else 0
    for i in range(dist):
        rope[0] = (rope[0][0] + xSpeed, rope[0][1] + ySpeed)
        for k in range(ROPELENGTH-1):
            head = rope[k]
            tail = rope[k + 1]
            if head[0] > tail[0]+1 or head[0] < tail[0]-1 or head[1] > tail[1]+1 or head[1] < tail[1]-1:
                moveX = max([-1, min([1, head[0] - tail[0]])])
                moveY = max([-1, min([1, head[1] - tail[1]])])
                tail = (tail[0] + moveX, tail[1] + moveY)
                rope[k+1] = tail
        visited.add(rope[ROPELENGTH - 1])
print("Places visited:", len(visited))
