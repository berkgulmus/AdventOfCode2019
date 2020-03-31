import numpy
import operator
dataFile = open("Day10_Data.txt")

asteroidCoordinates =[]
for corY,line in enumerate(dataFile):
    for corX,c in enumerate(line):
        if(c=="#"):
            asteroidCoordinates.append([corX,corY])

#answers from day 10.1
baseX = 20
baseY = 19



borders=[]#0 is up, 1 is right, 2 is down, 3 is left
areas =[]
##notation for areas and border------
##[x coordinate of asteroid, y coordinate of asteroid, distance from base, xDivY,yDivX,0 if it hasnot been killed & 1 if its]
for i in range(4):
    areas.append([])
    borders.append([])



#seperating values to areas or borders
for i in range(len(asteroidCoordinates)):
    astCordX =asteroidCoordinates[i][0]
    astCordY = asteroidCoordinates[i][1]
    #print(astCordX,astCordY)
    if(astCordX == baseX and astCordY == baseY):
        continue
    xDif= baseX - astCordX
    yDif = baseY- astCordY
    distanceFromBase = numpy.sqrt(xDif*xDif + yDif*yDif)


    #borders
    if(xDif==0):
        if(yDif>0):
            borders[0].append([astCordX,astCordY,distanceFromBase,0,0,0])
        elif(yDif<0):
            borders[2].append([astCordX, astCordY, distanceFromBase,0,0, 0])
        else:
            print("something is very wrong here dude")
            exit()
    elif (yDif == 0):
        if (xDif > 0):
            borders[3].append([astCordX, astCordY, distanceFromBase,0,0, 0])
        elif (xDif < 0):
            borders[1].append([astCordX, astCordY, distanceFromBase, 0,0,0])
        else:
            print("something is very wrong here dude")
            exit()


    #areas
    else:
        xDivY = xDif/yDif
        yDivX = yDif/xDif
        if(xDif< 0 and yDif >0):#area 1
            areas[0].append([astCordX, astCordY, distanceFromBase, xDivY,yDivX,0])
        elif (xDif < 0 and yDif < 0):#area 2
            areas[1].append([astCordX, astCordY, distanceFromBase, xDivY,yDivX,0])
        elif (xDif > 0 and yDif < 0):#area 3
            areas[2].append([astCordX, astCordY, distanceFromBase, xDivY,yDivX,0])
        elif (xDif > 0 and yDif > 0):#area 4
            areas[3].append([astCordX, astCordY, distanceFromBase, xDivY,yDivX,0])
        else:
            print("what the hell is happening right now man")
            exit()

areas[0].sort(key=lambda x: (-x[3], x[2]))
areas[1].sort(key=lambda x: (-x[3], x[2]))
areas[2].sort(key=lambda x: (-x[3], x[2]))
areas[3].sort(key=lambda x: (-x[3], x[2]))

borders[0].sort(key=operator.itemgetter(2))
borders[1].sort(key=operator.itemgetter(2))
borders[2].sort(key=operator.itemgetter(2))
borders[3].sort(key=operator.itemgetter(2))


destCtr=0 #destroyed counter
totalCount = 0
for i in range(4):
    totalCount+=len(borders[i])
    totalCount+=len(areas[i])

asteroid200th =0

while(True):
    for i in range(4):
        for j in range(len(borders[i])):
            if(borders[i][j][5]==0):
                destCtr+=1
                if(destCtr==200):
                    asteroid200th = str(borders[i][j][:2])
                borders[i][j][5]=1
                #print("popped "+ str(destCtr)+". asteroid at:"+str(borders[i][j][:2]))
                break
        lastPopped =0
        for j in range(len(areas[i])):
            if(areas[i][j][5]==0 and lastPopped != areas[i][j][3]):
                lastPopped=areas[i][j][3]
                destCtr+=1
                if(destCtr==200):
                    asteroid200th = str(areas[i][j][:2])
                areas[i][j][5] =1
                #print("popped " + str(destCtr) + ". asteroid at:" + str(areas[i][j][:2]))


    if(destCtr == totalCount):
        #print("NO MORE MUTANTS")
        break

print("200th asteroid is at:"+asteroid200th)