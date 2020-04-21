#This script solves 15.1 and shows the whole map after it's finished

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
                   # print("waiting input")
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


class PathFinder:
    def __init__(self,grid ):
        self.grid = grid
        self.alreadyLooked=[]
        self.toLook=[]
        self.path =[]
    def search(self,startPosX,startPosY,finishPosX,finishPosY):
        self.valueArray =[ [-1 for j in range(len(grid))] for i in range(len(grid))]
        self.valueArray[startPosX][startPosY]=0
        self.lookAround(startPosX,startPosY,finishPosX,finishPosY)
        while(len(self.toLook)!=0):
            toLookVal = self.toLook[0]
            res = self.lookAround(toLookVal[0],toLookVal[1],finishPosX,finishPosY)
            self.toLook.remove(toLookVal)
            if(res ==1):
                break
        self.createPath(finishPosX,finishPosY)

    def createPath(self,finishPosX,finishPosY):
        resVal = self.valueArray[finishPosX][finishPosY]
        currentVal =resVal
        curLocX,curLocY = finishPosX,finishPosY
        while(currentVal!=0):

            for i in range(1,5):
                targetX, targetY = curLocX, curLocY
                if (i == 1):
                    if (curLocY == 0):
                        continue
                    targetY -= 1
                elif (i == 2):
                    if (curLocY == len(self.grid) - 1):
                        continue
                    targetY += 1
                elif (i == 3):
                    if (curLocX == 0):
                        continue
                    targetX -= 1
                elif (i == 4):
                    if (curLocX == len(self.grid) - 1):
                        continue
                    targetX += 1

                if(self.valueArray[targetX][targetY] == currentVal-1):
                    curLocX,curLocY=targetX,targetY
                    currentVal = self.valueArray[targetX][targetY]
                    self.path.insert(0,i)
                    #(curLocX,curLocY,currentVal,i)
                    break
        self.reverseDirections()

    def reverseDirections(self):
        for i in range(len(self.path)):
            if(self.path[i]==1):
                self.path[i]=2
            elif(self.path[i] ==2):
                self.path[i]=1
            elif(self.path[i]==3):
                self.path[i]=4
            elif(self.path[i]==4):
                self.path[i]=3
            else:
                print("something is wrong mate")
    def lookAround(self,posX,posY,finishX,finishY):
        value = self.valueArray[posX][posY]
        self.alreadyLooked.append([posX,posY])
        gridVal = grid[posX][posY]
        if(posX == finishX and posY == finishY):
            return 1

        for i in range(1,5):
            targetX , targetY = posX,posY
            if(i==1):
                if(posY==0):
                    continue
                targetY-=1
            elif(i==2):
                if (posY == len(self.grid)-1):
                    continue
                targetY+=1
            elif(i==3):
                if (posX == 0):
                    continue
                targetX-=1
            elif(i==4):
                if (posX == len(self.grid)-1):
                    continue
                targetX+=1
            else:
                print("wtf is going on mate")
                exit()

            if((self.grid[targetX][targetY]==1 or self.grid[targetX][targetY] ==2) and [targetX,targetY] not in self.alreadyLooked):
                self.toLook.append([targetX,targetY])
                if(self.valueArray[targetX][targetY]==-1 or (self.valueArray[targetX][targetY] != -1 and self.valueArray[targetX][targetY] > value)):
                    self.valueArray[targetX][targetY] = value+1

        return 0


    def showValueArray(self):
        for i in range(len(self.valueArray)):
            for j in range(len(self.valueArray)):
                print(self.valueArray[j][i],end=" / ")

            print("")


    def showGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                print(self.grid[j][i],end=" / ")

            print("")



def goFromXtoY(start,finish):
    pFinder = PathFinder(grid)
    pFinder.search(start[0],start[1],finish[0],finish[1])
    for i in range(len(pFinder.path)):
        movePlayer(pFinder.path[i])
    return len(pFinder.path)

def lookAround():
    global posX, posY
    posMoves =[]#possible moves
    for i in range(1, 5):
        res = movePlayer(i)
        if (res ==0):
            continue
        else:
            #(directionToPosition(i))
            movePlayer(reverseDirection(i))
            posMoves.append([directionToPosition(i),i])
    tempArr =[]
    for i in posMoves:
        if(i[0] not in alreadyLooked):
            tempArr.append(i)
    alreadyLooked.append([posX,posY])

    return tempArr

def reverseDirection(direction:int):
    reverse =0
    if(direction==1):
        reverse=2
    elif(direction==2):
        reverse=1
    elif(direction==3):
        reverse=4
    elif(direction==4):
        reverse=3
    return reverse

def directionToPosition(direction:int):
    global posX,posY
    if (direction == 1):
        return [posX,posY-1]
    elif (direction == 2):
        return [posX, posY + 1]
    elif (direction == 3):
        return [posX -1, posY ]
    elif (direction == 4):
        return [posX + 1, posY]


def movePlayer(direction):
    global posX,posY
    intComp0.addInput(direction)
    intComp0.compute()
    result = intComp0.getOutput()[0]
    #print(posX, posY, direction, result)
    intComp0.flushOutputs()
    targetPosX = posX
    targetPosY = posY

    if (direction == 1):  # up
        targetPosY -= 1
    elif (direction == 2):  # down
        targetPosY += 1
    elif (direction == 3):  # left
        targetPosX -= 1
    elif (direction == 4):  # right
        targetPosX += 1
    if (targetPosX >= 0 and targetPosX <=gridSize and targetPosY >= 0 and targetPosY < gridSize):
        if (result == 0):
            grid[targetPosX][targetPosY] = 0 # -1=undiscovered, 0=wall, 1=free, 2=oxygen,
            return result
        elif (result == 1):
            grid[targetPosX][targetPosY] = 1
            posX = targetPosX
            posY = targetPosY
            return result
        elif (result == 2):
            grid[targetPosX][targetPosY] = 2
            posX = targetPosX
            posY = targetPosY
            return result
    else:
        print("we've gone beyond grid, shutting down")
        exit()
    #print(posX,posY)

def drawGrid(screen):
    screen.fill((210, 251, 255))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            color = (255, 255, 255)
            if (grid[i][j] == -1):
                color = (183, 97, 34)
            elif (grid[i][j] == 0):
                color = (26, 26, 28)
            elif (grid[i][j] == 1):
                color = (242, 224, 189)
            elif (grid[i][j] == 2):
                color = (31, 239, 255)
            pygame.draw.rect(screen, color, [i * boxX, j * boxY, boxX, boxY])
    pygame.draw.circle(screen, (82, 145, 50), [int(posX * boxX + boxX / 2), int(posY * boxY + boxY / 2)], 5)
    pygame.display.flip()
    pygame.time.Clock().tick(60)










data = open("Day15_Data.txt").read().split(",")
for i in range(len(data)):
    data[i] = int(data[i])
intComp0 = intCodeComputer(data, 0)


gridSize = 80
grid = []
for i in range(gridSize):
    grid.append([])
    for j in range(gridSize):
        grid[i].append(-1)

posX = posY = int(gridSize / 2)  # starting position
grid[posX][posY] = 1

alreadyLooked=[]
nextStep =[]
divergence=[]



while(True):
    posMoves =lookAround()
    if(len(posMoves)==0):
        if(len(divergence)>0):
            goFromXtoY([posX,posY],divergence[0])
            divergence.pop(0)
        else:
            break
    elif(len(posMoves)==1):
        goFromXtoY([posX,posY],posMoves[0][0])
    else:
        goFromXtoY([posX, posY], posMoves[0][0])
        for i in range(1,len(posMoves)):
            divergence.append(posMoves[i][0])


oxygenSourcePos=[]
for i in range(len(grid)):
    found=False

    for j in range(len(grid[i])):
        a= grid[i][j]
        if(grid[i][j]==2):

            oxygenSourcePos.append(i)
            oxygenSourcePos.append(j)
            found=True
            break
    if(found):
        break

print(oxygenSourcePos)
goFromXtoY([posX,posY],[int(gridSize/2),int(gridSize/2)])
pathLength = goFromXtoY([int(gridSize/2),int(gridSize/2)],oxygenSourcePos)
print(pathLength)






import pygame

pygame.init()
boxX = boxY = 10
screenX = screenY = 810
screen = pygame.display.set_mode([screenX, screenY])
screen.fill((210, 251, 255))

running= True
print(grid)
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawGrid(screen)