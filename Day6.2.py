class Planet:

    def __init__(self,name):
        self.name=name
        self.orbitsIndex = -5
        self.planetsOrbiting = []
        self.lengthFromCom = -5
    def addOrbitingPlanet(self,index):
        self.planetsOrbiting.append(index)


def planetExists(name):
    for i in range(len(Planets)):
        if(Planets[i].name == name):
            return i
    return -1




DataFile = open("Day6_Data.txt")
Data= DataFile.readlines()

Planets=[]
for i in range(len(Data)):
    split = Data[i][:-1].split((")"))

    indexX = planetExists(split[0])
    if(indexX==-1):
        newPlanet=0
        newPlanet = Planet(split[0])

        Planets.append(newPlanet)
        indexX=len(Planets)-1

    indexY = planetExists(split[1])
    if (indexY == -1):
        newPlanet2=0
        newPlanet2 = Planet(split[1])

        Planets.append(newPlanet2)
        indexY = len(Planets) - 1

    Planets[indexX].addOrbitingPlanet(indexY)
    Planets[indexY].orbitsIndex=indexX

sanIndex = 0
for i in range(len(Planets)):
    if(Planets[i].name=="SAN"):
        sanIndex=i
        break


curLenght =0
toLook =[]
toLook.append(sanIndex)
alreadyLooked=[]
while(True):
    tempToLook=[]
    for i in range(len(toLook)):
        if(toLook[i] not in alreadyLooked):
            toLookLocal = Planets[toLook[i]].planetsOrbiting.copy()
            toLookLocal.append(Planets[toLook[i]].orbitsIndex)
            for j in range(len(toLookLocal)):
                if(toLookLocal[j] not in alreadyLooked):
                    if(Planets[toLookLocal[j]].name=="YOU"):
                        print(curLenght-1)
                        exit()
                    else:
                        tempToLook.append(toLookLocal[j])
            alreadyLooked.append(toLook[i])
    toLook = tempToLook.copy()
    curLenght+=1




