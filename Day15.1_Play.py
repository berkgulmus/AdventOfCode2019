#You can move around and try to find the oxygen source with this
#although you're much more likely to give up before you can actually find it tbh
class intCodeComputer:
    def __init__(self, programCode, id=0, relBase=0, indx=0, emptySpace=1000, inptArr=[]):
        self.relativeBase = 0
        self.memory = []
        self.memory = programCode.copy()
        for i in range(emptySpace):
            self.memory.append(0)
        self.index = indx
        self.inputArray = inptArr.copy()
        self.outputArray = []
        self.id = id
        self.finished = False

    def setSingleMemoryAddress(self, pos, val):
        self.memory[pos] = val

    def compute(self):  # computes until there's an input requiered

        while (not self.finished):

            if (self.index == 308):
                print(self.memory[311])
            # formatting OPCODE

            TempLen = len(str(self.memory[self.index]))
            StringToAdd = ""
            for i in range(5 - TempLen):
                StringToAdd += "0"
            self.memory[self.index] = StringToAdd + str(self.memory[self.index])
            # print(self.memory[self.index])

            # reading parameters according to the given parameter modes ----------------------
            parameters = []
            parameterMode = str(self.memory[self.index][:3])
            # print(self.memory[self.index], parameterMode)
            # print(parameterMode)
            OpCode = str(self.memory[self.index])[-2:]
            self.memory[self.index] = int(self.memory[self.index])
            if (parameterMode[2] == "0"):
                parameters.append(int(self.memory[self.index + 1]))
            elif (parameterMode[2] == "1"):
                parameters.append(self.index + 1)
            else:  # paramMode 2
                parameters.append(int(self.memory[self.index + 1]) + self.relativeBase)

            if (parameterMode[1] == "0"):
                parameters.append(int(self.memory[self.index + 2]))
            elif (parameterMode[1] == "1"):
                parameters.append(self.index + 2)
            else:  # paramMode 2
                parameters.append(self.memory[self.index + 2] + self.relativeBase)

            if (parameterMode[0] == "0"):
                parameters.append(int(self.memory[self.index + 3]))
            elif (parameterMode[0] == "1"):
                parameters.append(self.index + 3)
            else:  # paramMode 2
                parameters.append(int(self.memory[self.index + 3]) + self.relativeBase)
            # param read end -----------------------------------------
            # strr=""
            # for i in range(4):
            #    strr += str(self.memory[self.index + i ] ) +"/"
            # print(self.index,strr,OpCode)
            # strr2 =""
            # for i in range(3):
            # strr2 += str(self.memory[parameters[i]] ) +"/"
            # print(strr2)
            # print("opcode:" + str(OpCode) + "  parameters: " + str(self.memory[parameters[0]]) +"/"+ str(
            # self.memory[parameters[1]]) +"/"+ str(self.memory[parameters[2]]))

            # reacting according to the OP CODE-----------------------------------------
            if (OpCode == "01"):
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) + int(self.memory[parameters[1]])
                self.index += 4
            elif (OpCode == "02"):
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) * int(self.memory[parameters[1]])
                self.index += 4
            elif (OpCode == "03"):
                if (len(self.inputArray) != 0):
                    self.memory[parameters[0]] = self.inputArray[0]
                    self.index += 2
                    self.inputArray.pop(0)
                else:
                    print("waiting input")
                    break
            elif (OpCode == "04"):
                # print("output from int comp "+str(self.id)+ "  :" +str(self.memory[parameters[0]]))
                self.outputArray.append(self.memory[parameters[0]])
                self.index += 2
            elif (OpCode == "05"):
                if (self.memory[parameters[0]] != 0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif (OpCode == "06"):
                # print("went here")
                if (self.memory[parameters[0]] == 0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif (OpCode == "07"):
                if (int(self.memory[parameters[0]]) < int(self.memory[parameters[1]])):
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif (OpCode == "08"):
                if (self.memory[parameters[0]] == self.memory[parameters[1]]):
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif (OpCode == "09"):
                self.relativeBase += self.memory[parameters[0]]
                self.index += 2
                # print("relative base has been changed")
            elif (OpCode == "99"):
                print(str(self.id) + ". computer has finished")
                self.finished = True
                break

            # print(self.relativeBase)

    def addInput(self, input):
        self.inputArray.append(input)

    def printOutputs(self):
        print(self.outputArray)

    def getOutput(self):
        return self.outputArray

    def flushOutputs(self):
        self.outputArray.clear()


def drawGrid(screen):
    screen.fill((210, 251, 255))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            color = (255, 255, 255)
            if (grid[i][j] == 0):
                color = (181, 123, 139)
            elif (grid[i][j] == 1):
                color = (158, 255, 248)
            elif (grid[i][j] == 2):
                color = (179, 153, 93)
            elif (grid[i][j] == 3):
                color = (255, 92, 138)
            pygame.draw.rect(screen, color, [i * boxX, j * boxY, boxX, boxY])
    pygame.draw.circle(screen, (255, 0, 0), [int(posX * boxX + boxX / 2), int(posY * boxY + boxY / 2)], 5)
    pygame.display.flip()
    pygame.time.Clock().tick(60)


def lookAround(intComp, posX, posY):
    for i in range(1, 5):
        resultX, resultY,res = movePlayer(intComp, i, posX, posY)
        if (resultX == posX and resultY == posY):
            continue
        else:
            if (i == 1):
                movePlayer(intComp, 2, posX, posY - 1)
            elif (i == 2):
                movePlayer(intComp, 1, posX, posY + 1)
            elif (i == 3):
                movePlayer(intComp, 4, posX - 1, posY)
            elif (i == 4):
                movePlayer(intComp, 3, posX + 1, posY)


def movePlayer(intComp, inputForIntComp, posX, posY):
    intComp.addInput(inputForIntComp)
    intComp.compute()
    result = intComp.getOutput()[0]
    print(posX, posY, inputForIntComp, result)
    intComp.flushOutputs()

    targetPosX = posX
    targetPosY = posY

    if (inputForIntComp == 1):  # up
        targetPosY -= 1
    elif (inputForIntComp == 2):  # down
        targetPosY += 1
    elif (inputForIntComp == 3):  # left
        targetPosX -= 1
    elif (inputForIntComp == 4):  # right
        targetPosX += 1
    if (targetPosX >= 0 and targetPosX <= gridSize and targetPosY >= 0 and targetPosY <= gridSize):
        if (result == 0):
            grid[targetPosX][targetPosY] = 2
            print(posX, posY, targetPosX, targetPosY)
            return posX, posY, result
        elif (result == 1):
            grid[targetPosX][targetPosY] = 1
            posX = targetPosX
            posY = targetPosY
            print(posX, posY, targetPosX, targetPosY)
            if ([targetPosX, targetPosY] not in alreadyLooked):
                placesToLook.insert(0, inputForIntComp)
                alreadyLooked.append([targetPosX, targetPosY])
            return targetPosX, targetPosY, result
        elif (result == 2):
            grid[targetPosX][targetPosY] = 3
            posX = targetPosX
            posY = targetPosY
            print(posX, posY, targetPosX, targetPosY)
            print("we've found it")
            exit()
            return targetPosX, targetPosY, result
    else:
        print("we've gone beyond grid, shutting down")
        exit()


import pygame

pygame.init()
boxX = boxY = 10
screenX = screenY = 810
screen = pygame.display.set_mode([screenX, screenY])
screen.fill((210, 251, 255))

breadCrumbs = []  # this will keep a record of my movement so i can go back
alreadyLooked = []
placesToLook = []

data = open("Day15_Data.txt").read().split(",")
for i in range(len(data)):
    data[i] = int(data[i])
intComp0 = intCodeComputer(data, 0)

gridSize = 80
grid = []
for i in range(gridSize):
    grid.append([])
    for j in range(gridSize):
        grid[i].append(0)

posX = posY = int(gridSize / 2)  # starting position
grid[posX][posY] = 1
# grid values, 0 unkown, 1 empty space, 2 wall, 3 oxygen unit
running = True
drawGrid(screen)
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT):
                posX, posY, res = movePlayer(intComp0, 3, posX, posY)
                lookAround(intComp0, posX, posY)
                drawGrid(screen)
            elif (event.key == pygame.K_RIGHT):
                posX, posY, res = movePlayer(intComp0, 4, posX, posY)
                lookAround(intComp0, posX, posY)
                drawGrid(screen)
            elif (event.key == pygame.K_DOWN):
                posX, posY, res = movePlayer(intComp0, 2, posX, posY)
                lookAround(intComp0, posX, posY)
                drawGrid(screen)
            elif (event.key == pygame.K_UP):
                posX, posY, res = movePlayer(intComp0, 1, posX, posY)
                lookAround(intComp0, posX, posY)
                drawGrid(screen)
            elif (event.key == pygame.K_SPACE):
                lookAround(intComp0, posX, posY)
                drawGrid(screen)

