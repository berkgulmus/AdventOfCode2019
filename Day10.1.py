dataFile = open("Day10_Data.txt")

asteroidCoordinates =[]
for corY,line in enumerate(dataFile):
    for corX,c in enumerate(line):
        if(c=="#"):
            asteroidCoordinates.append([corX,corY])


curMax=0
astBaseX = astBaseY =0
for astBase in range( len(asteroidCoordinates)):
    seenDivisionsR = []
    seenDivisionsL =[]
    seenAsteroids =[]
    foundRight = foundLeft = foundUp = foundDown = False
    foundCount =0
    for observeAst in range(len(asteroidCoordinates)):
        if(asteroidCoordinates[astBase][0] >= asteroidCoordinates[observeAst][0]):
            if(astBase == observeAst):
                continue
            asteroidX = asteroidCoordinates[observeAst][0]
            asteroidY = asteroidCoordinates[observeAst][1]
            xDifference = asteroidCoordinates[astBase][0] - asteroidX
            yDifference = asteroidCoordinates[astBase][1] - asteroidY
            if(yDifference==0):
                if(xDifference>0):
                    if(not foundLeft):
                        foundLeft = True
                        seenAsteroids.append([asteroidX, asteroidY])
                else:
                    if(not foundRight):
                        foundRight=True
                        seenAsteroids.append([asteroidX, asteroidY])
            elif (xDifference == 0):
                if (yDifference > 0):
                    if(not foundUp):
                        foundUp = True
                        seenAsteroids.append([asteroidX, asteroidY])
                else:
                    if(not foundDown):
                        foundDown = True
                        seenAsteroids.append([asteroidX, asteroidY])
            else:
                div = xDifference/yDifference
                if(div not in seenDivisionsR):
                    seenDivisionsR.append(div)
                    seenAsteroids.append([asteroidX,asteroidY])

        else:
            if (astBase == observeAst):
                continue
            asteroidX = asteroidCoordinates[observeAst][0]
            asteroidY = asteroidCoordinates[observeAst][1]
            xDifference = asteroidCoordinates[astBase][0] - asteroidX
            yDifference = asteroidCoordinates[astBase][1] - asteroidY
            if (yDifference == 0):
                if (xDifference > 0):
                    if(not foundLeft):
                        foundLeft = True
                        seenAsteroids.append([asteroidX, asteroidY])
                else:
                    if(not foundRight):
                        foundRight = True
                        seenAsteroids.append([asteroidX, asteroidY])
            elif (xDifference == 0):
                if (yDifference > 0):
                    if(not foundUp):
                        foundUp = True
                        seenAsteroids.append([asteroidX, asteroidY])
                else:
                    if(not foundDown):
                        foundDown = True
                        seenAsteroids.append([asteroidX, asteroidY])
            else:
                div = xDifference / yDifference
                if (div not in seenDivisionsL):
                    seenDivisionsL.append(div)
                    seenAsteroids.append([asteroidX, asteroidY])

    foundCount =len(seenAsteroids)
    print(foundCount,seenAsteroids)
    if(foundCount>curMax):
        astBaseX=asteroidCoordinates[astBase][0]
        astBaseY = asteroidCoordinates[astBase][1]
        curMax = foundCount
print(curMax,astBaseX,astBaseY)