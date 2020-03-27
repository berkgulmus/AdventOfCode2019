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

def remainedUncalculated():
    for i in range(len(Planets)):
        if(Planets[i].lengthFromCom==-5):
            return True
    return False


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

ToBeCalculated = []

for i in range(len(Planets)):
    if(Planets[i].name=="COM"):
        for j in range(len(Planets[i].planetsOrbiting)):
            Planets[Planets[i].planetsOrbiting[j]].lengthFromCom=1
            ToBeCalculated.append(Planets[i].planetsOrbiting[j])
        Planets[i].lengthFromCom=0
        break

while(remainedUncalculated()):
    TempList =[]
    for i in range(len(ToBeCalculated)):
        OrbitCount = len(Planets[ToBeCalculated[i]].planetsOrbiting)
        for j in range(OrbitCount):
            Planets[Planets[ToBeCalculated[i]].planetsOrbiting[j]].lengthFromCom = Planets[ToBeCalculated[i]].lengthFromCom+1
            TempList.append(Planets[ToBeCalculated[i]].planetsOrbiting[j])

    ToBeCalculated=[]
    ToBeCalculated=TempList.copy()

Total =0
for i in range(len(Planets)):
    Total+=Planets[i].lengthFromCom
    print(Planets[i].lengthFromCom)
print(Total)