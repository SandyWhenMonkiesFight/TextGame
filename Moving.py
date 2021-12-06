f = open("Map.txt", "r")

values = f.read()

Map = values.split("\n")

for counter in range(len(Map)):
    Map[counter] = Map[counter].split(",")

print(Map)

#Map[x][y]

X = 3
Y = 3

def movement(currentX, currentY):
    answer = input()
    if answer == "w":
        if currentY != 1:
            currentY -= 1
        print("You are at " + Map[currentY - 1][currentX - 1])
    if answer == "a":
        if currentX != 1:
            currentX -= 1
        print("You are at " + Map[currentY - 1][currentX - 1])
    if answer == "s":
        if currentY != len(Map):
            currentY += 1
        print("You are at " + Map[currentY - 1][currentX - 1])
    if answer == "d":
        if currentX != len(Map):
            currentX += 1
        print("You are at " + Map[currentY - 1][currentX - 1])
    return currentX, currentY
    
#Test code           
while True:
    X, Y = movement(X, Y)
