class intCodeComputer:
    def __init__(self,programCode,id =0, relBase=0,indx=0,emptySpace=1000,inptArr=[]):
        self.relativeBase =0
        self.memory =[]
        self.memory = programCode.copy()
        for i in range(emptySpace):
            self.memory.append(0)
        self.index=indx
        self.inputArray=inptArr.copy()
        self.outputArray=[]
        self.id=id
        self.finished = False

    def setSingleMemoryAddress(self,pos,val):
        self.memory[pos]=val
    def compute(self):#computes until there's an input requiered

        while(not self.finished):

            if(self.index == 308):
                print(self.memory[311])
            #formatting OPCODE

            TempLen = len(str(self.memory[self.index]))
            StringToAdd = ""
            for i in range(5 - TempLen):
                StringToAdd += "0"
            self.memory[self.index] = StringToAdd + str(self.memory[self.index])
            #print(self.memory[self.index])


            #reading parameters according to the given parameter modes ----------------------
            parameters = []
            parameterMode = str(self.memory[self.index][:3])
            #print(self.memory[self.index], parameterMode)
            #print(parameterMode)
            OpCode = str(self.memory[self.index])[-2:]
            self.memory[self.index]=int(self.memory[self.index])
            if (parameterMode[2] == "0"):
                parameters.append(int(self.memory[self.index + 1]))
            elif (parameterMode[2] == "1"):
                parameters.append(self.index + 1)
            else:#paramMode 2
                parameters.append(int(self.memory[self.index + 1]) +self.relativeBase)

            if (parameterMode[1] == "0"):
                parameters.append(int(self.memory[self.index + 2]))
            elif (parameterMode[1] == "1"):
                parameters.append(self.index + 2)
            else:#paramMode 2
                parameters.append(self.memory[self.index + 2] + self.relativeBase)


            if (parameterMode[0] == "0"):
                parameters.append(int(self.memory[self.index + 3]))
            elif (parameterMode[0] == "1"):
                parameters.append(self.index + 3)
            else:#paramMode 2
                parameters.append(int(self.memory[self.index + 3]) + self.relativeBase)
            #param read end -----------------------------------------
            #strr=""
            #for i in range(4):
            #    strr += str(self.memory[self.index + i ] ) +"/"
            #print(self.index,strr,OpCode)
            #strr2 =""
            #for i in range(3):
                #strr2 += str(self.memory[parameters[i]] ) +"/"
            #print(strr2)
            #print("opcode:" + str(OpCode) + "  parameters: " + str(self.memory[parameters[0]]) +"/"+ str(
                #self.memory[parameters[1]]) +"/"+ str(self.memory[parameters[2]]))

            #reacting according to the OP CODE-----------------------------------------
            if(OpCode=="01"):
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) + int(self.memory[parameters[1]])
                self.index +=4
            elif(OpCode=="02"):
                self.memory[parameters[2]] = int(self.memory[parameters[0]]) * int(self.memory[parameters[1]])
                self.index += 4
            elif(OpCode=="03"):
                if(len(self.inputArray)!=0):
                    self.memory[parameters[0]]=self.inputArray[0]
                    self.index+=2
                    self.inputArray.pop(0)
                else:
                    print("waiting input")
                    break
            elif(OpCode=="04"):
                #print("output from int comp "+str(self.id)+ "  :" +str(self.memory[parameters[0]]))
                self.outputArray.append(self.memory[parameters[0]])
                self.index+=2
            elif(OpCode=="05"):
                if(self.memory[parameters[0]]!=0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index+=3
            elif(OpCode=="06"):
               # print("went here")
                if (self.memory[parameters[0]] == 0):
                    self.index = int(self.memory[parameters[1]])
                else:
                    self.index += 3
            elif(OpCode=="07"):
                if(int(self.memory[parameters[0]]) < int(self.memory[parameters[1]])):
                    self.memory[parameters[2]]=1
                else:
                    self.memory[parameters[2]]=0
                self.index+=4
            elif(OpCode=="08"):
                if (self.memory[parameters[0]] == self.memory[parameters[1]]):
                    self.memory[parameters[2]] = 1
                else:
                    self.memory[parameters[2]] = 0
                self.index += 4
            elif(OpCode=="09"):
                self.relativeBase += self.memory[parameters[0]]
                self.index+=2
                #print("relative base has been changed")
            elif(OpCode=="99"):
                print(str(self.id)+ ". computer has finished")
                self.finished=True
                break

            #print(self.relativeBase)

    def addInput(self,input):
        self.inputArray.append(input)

    def printOutputs(self):
        print(self.outputArray)

    def getOutput(self):
        return  self.outputArray

    def flushOutputs(self):
        self.outputArray.clear()


import pygame

pygame.init()
boxX = boxY = 10
screenX = screenY = 500
screen= pygame.display.set_mode([screenX,screenY])
screen.fill((210,251,255))



data = open("Day13_Data.txt").read().split(",")
for i in range(len(data)):
    data[i]=int(data[i])
comp0 = intCodeComputer(data,0)
comp0.setSingleMemoryAddress(0,2)
comp0.compute()
outArr = comp0.getOutput()
ballPosX = paddlePosX = 0
score =0
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if True:
        inputForPaddle = 0
        if(ballPosX > paddlePosX):
            inputForPaddle = 1
        elif(ballPosX < paddlePosX):
            inputForPaddle = -1

        comp0.addInput(inputForPaddle)
        comp0.compute()
        print(score)

    #clear screen
    screen.fill((150,170,60))
    #populate screen
    for i in range(0, len(outArr), 3):
        if(outArr[i] == -1 and outArr[i+1] == 0):
            score = outArr[i+2]

        else:
            color = (255,255,255)
            if(outArr[i+2] == 0):
                color = (161, 228, 255)
            elif(outArr[i+2] == 1):
                color = (204, 131, 108)
            elif(outArr[i+2] == 2):
                color = (108, 126, 204)
            elif(outArr[i+2] == 3):
                color = (35, 57, 153)
                paddlePosX = outArr[i ]
            elif(outArr[i + 2] == 4):
                color = (250, 187, 149)
                ballPosX=outArr[i]
            elif (outArr[i + 2] == 4):
                color = (250, 187, 149)
                ballPosX = outArr[i]
            else:
                print("something is wrong here my dude")
                exit()
            rect1 = pygame.draw.rect(screen, color, [outArr[i]*boxX,outArr[i+1]*boxY,boxX,boxY])
    pygame.display.flip()
    pygame.time.Clock().tick(60)


print(score)