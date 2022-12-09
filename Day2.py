A = 'A'
B = 'B'
C = 'C'
X = 'X'
Y = 'Y'
Z = 'Z'
WIN = 6
LOSS = 0
DRAW = 3
SHAPESCORE = {A: 1, B: 2, C: 3, X: 1, Y: 2, Z: 3}
CODETOSTRAT = {X: LOSS, Y: DRAW, Z: WIN}
OUTCOME = {A: {X: DRAW, Y: WIN, Z: LOSS}, B: {X: LOSS, Y: DRAW, Z: WIN}, C: {X: WIN, Y: LOSS, Z: DRAW}}
STRATEGY = {A: {WIN: Y, DRAW: X, LOSS: Z}, B: {WIN: Z, DRAW: Y, LOSS: X}, C: {WIN: X, DRAW: Z, LOSS: Y}}

f = open("resources/day2_input.txt", "r")
lines = f.read().splitlines()
p1score = 0
p2score = 0
for line in lines:
    move = line.split()
    p1score += SHAPESCORE[move[1]] + OUTCOME[move[0]][move[1]]
    outcome = CODETOSTRAT[move[1]]
    p2score += SHAPESCORE[STRATEGY[move[0]][outcome]] + outcome
print("Total score part1:", p1score)
print("Total score part2:", p2score)
