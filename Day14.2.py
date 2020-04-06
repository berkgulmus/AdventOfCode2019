

def getId(name):
    for i,ing in enumerate(inventory):
        if(ing[0] == name):
            return i
    return -1

def getRecipeId(name):
    for i,line in enumerate(lines):
        if(line[1][1]==name):
            return i
    return  -1
oreCount = 1000000000000
oreNeedForOne = 278404
def createFuel():
    global inventory,oreCount,fuelCreated,oreNeedForOne
    ##we get this input from first part of the day 14
    inventory2 = [['RJLWC', 5], ['RJCH', 3], ['QWFH', 0], ['XZVHQ', 5], ['SPQR', 7], ['WKGVW', 0], ['KPZB', 4], ['HPRPM', 3], ['GTZCK', 3], ['DJNDX', 5], ['JKRV', 4], ['FKTLR', 0], ['FDSBZ', 3], ['VTCRJ', 6], ['SPSW', 2], ['KBJF', 0], ['QHVSJ', 0], ['TFPNF', 5], ['MNMBX', 0], ['QCMJ', 2], ['TXPL', 2], ['VQPX', 4], ['GPKR', 0], ['DWTC', 0], ['DSPJG', 0], ['ORE', 0], ['XZDP', 4], ['DBRBD', 3], ['DKRX', 0], ['VXZN', 0], ['HWDS', 1], ['ZRBN', 1], ['QNXZV', 3], ['LJQH', 2], ['FKXVQ', 2], ['DZGN', 0], ['HWJVK', 4], ['FUEL', 0], ['GSLWP', 2], ['PWTFL', 3], ['HVPWG', 1], ['NVWGS', 0], ['CWZRS', 5], ['XPMV', 1], ['JZDB', 3], ['BWXWC', 0], ['HKFD', 0], ['FMNK', 0], ['VMHM', 8], ['ZSKSW', 0], ['ZTFZG', 7], ['FGQF', 2], ['VLQP', 2], ['TGLHX', 3], ['GQGB', 0], ['FDSZX', 0], ['TJLW', 1], ['MPSPS', 0], ['RWKWD', 0], ['GKVQK', 1]]


    multiplier = int(oreCount / oreNeedForOne)
    oreCount = oreCount - oreNeedForOne*multiplier
    fuelCreated+=multiplier
    for i,item in enumerate(inventory):
        if(item[0]!='ORE'):
            item[1] += inventory2[i][1]*multiplier

    inventory[getId("ORE")][1]+=oreCount

def deconstruct():
    #---------------------
    #deconstruct everything we possibly can
    global inventory,oreCount

    controlFlag = True
    while(controlFlag):
        controlFlag = False
        #print(inventory)
        for item in inventory:
            if(item[0] in ["ORE","FUEL"]):
                continue
            recipeId = getRecipeId(item[0])
            multiplier=int(item[1] /int(lines[recipeId][1][0]))
           # print(item[1],lines[recipeId][1][0],multiplier)
          #  print("*",int(lines[recipeId][1][0])*multiplier)
            if(multiplier==0):
                continue
            else:
                controlFlag= True
                #print("before",item[1])
                item[1] -= multiplier*int(lines[recipeId][1][0])
               # print("after",item[1])
                for ingredient in lines[recipeId][0]:
                    if(ingredient[1]=="ORE"):
                        oreCount+=multiplier* int(ingredient[0])
                    else:
                        inventory[getId(ingredient[1])][1] += multiplier* int(ingredient[0])

    print(inventory)

def loopForever():
    global oreCount,oreNeedForOne,fuelCreated
    while(oreCount>=oreNeedForOne):
        createFuel()
        deconstruct()
    print(fuelCreated)

inventory =[]
fuelCreated = 0

lines = open("Day14_Data.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip('\n').split(" => ")
    lines[i][0] = lines[i][0].split(", ")
    lines[i][1] = lines[i][1].split(" ")
    for j in range(len(lines[i][0])):
        lines[i][0][j]=lines[i][0][j].split(" ")

for line in lines:
    ingredients = line[0]
    for words in ingredients:
        name = words[1]

        if [name,0] not in inventory:
            inventory.append([name,0])
    name = line[1][1]
    if [name, 0] not in inventory:
        inventory.append([name, 0])

print(inventory)
loopForever()



