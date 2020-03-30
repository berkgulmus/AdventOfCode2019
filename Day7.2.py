from itertools import permutations
ended = False
Data_File = open("Day7_Data.txt")
DataOriginal = Data_File.read()
DataOriginal = DataOriginal.split(',')
#for i in range(len(Data)):
   # Data[i]=int(Data[i])

Numbers = [ 5,6,7,8,9]
allPossibleCombinations = list(permutations(Numbers,r=5))
currentMost = 0
currentWinningOrder =[]
indexArr =[]
def Circuit(systemIndex):
    IndexNumber = indexArr[systemIndex]
    #print(str(systemIndex+1)+". module started at " + str(IndexNumber) + " with input : " + str(inputArr[systemIndex][0]))
    Data = dataArr[systemIndex]
    endedCircuit = False
    while (not endedCircuit):
        TempLen = len(str(Data[IndexNumber]))
        StringToAdd = ""
        for i in range(5 - TempLen):
            StringToAdd += "0"
        Data[IndexNumber] = StringToAdd + str(Data[IndexNumber])
        FullCode = str(Data[IndexNumber])
        OpCode = Data[IndexNumber][-2:]
        if (OpCode == "01"):
            NumbToAdd1 = NumbToAdd2 = 0
            if (FullCode[2] == "0"):
                NumbToAdd1 = Data[int(Data[IndexNumber + 1])]
            else:
                NumbToAdd1 = Data[IndexNumber + 1]

            if (FullCode[1] == "0"):
                NumbToAdd2 = Data[int(Data[IndexNumber + 2])]
            else:
                NumbToAdd2 = Data[IndexNumber + 2]
            if (FullCode[0] == "0"):
                PlaceToWrite = int(Data[IndexNumber + 3])
            else:
                PlaceToWrite = IndexNumber + 3
            Data[PlaceToWrite] = int(NumbToAdd1) + int(NumbToAdd2)
            IndexNumber += 4
        elif (OpCode == "02"):
            NumbToMultiply1 = NumbToMultiply2 = 0
            if (FullCode[2] == "0"):
                NumbToMultiply1 = Data[int(Data[IndexNumber + 1])]
            else:
                NumbToMultiply1 = Data[IndexNumber + 1]

            if (FullCode[1] == "0"):
                NumbToMultiply2 = Data[int(Data[IndexNumber + 2])]
            else:
                NumbToMultiply2 = Data[IndexNumber + 2]

            if (FullCode[0] == "0"):
                PlaceToWrite = int(Data[IndexNumber + 3])
            else:
                PlaceToWrite = IndexNumber + 3

            Data[PlaceToWrite] = int(NumbToMultiply1) * int(NumbToMultiply2)

            IndexNumber += 4
        elif (OpCode == "03"):
            userinput = inputArr[systemIndex][0]
            del inputArr[systemIndex][0]

            if (FullCode[2] == "0"):
                PlaceToWrite = int(Data[IndexNumber + 1])
            else:
                PlaceToWrite = IndexNumber + 1

            Data[PlaceToWrite] = int(userinput)
            IndexNumber += 2
        elif (OpCode == "04"):
            NumbToWrite = 0
            if (FullCode[2] == "0"):
                NumbToWrite = Data[int(Data[IndexNumber + 1])]
            else:
                NumbToWrite = int(Data[IndexNumber + 1])

            IndexNumber += 2
            #print(str(systemIndex+1)+". module stopped at " + str(IndexNumber) + "    with output : "+ str(NumbToWrite))
            indexArr[systemIndex]= IndexNumber
            return NumbToWrite
        elif (OpCode == "05"):
            FirstP = SecondP = 0
            if (FullCode[2] == "0"):
                FirstP = Data[int(Data[IndexNumber + 1])]
            else:
                FirstP = Data[IndexNumber + 1]

            if (FullCode[1] == "0"):
                SecondP = Data[int(Data[IndexNumber + 2])]
            else:
                SecondP = Data[IndexNumber + 2]

            if (str(FirstP) != "0"):
                IndexNumber = int(SecondP)
            else:
                IndexNumber += 3

        elif (OpCode == "06"):
            FirstP = SecondP = 0
            if (FullCode[2] == "0"):
                FirstP = Data[int(Data[IndexNumber + 1])]
            else:
                FirstP = Data[IndexNumber + 1]

            if (FullCode[1] == "0"):
                SecondP = Data[int(Data[IndexNumber + 2])]
            else:
                SecondP = Data[IndexNumber + 2]

            if (str(FirstP) == "0"):
                IndexNumber = int(SecondP)
            else:
                IndexNumber += 3

        elif (OpCode == "07"):
            FirstP = SecondP = ThirdP = 0
            if (FullCode[2] == "0"):
                FirstP = Data[int(Data[IndexNumber + 1])]
            else:
                FirstP = Data[IndexNumber + 1]

            if (FullCode[1] == "0"):
                SecondP = Data[int(Data[IndexNumber + 2])]
            else:
                SecondP = Data[IndexNumber + 2]

            if (FullCode[0] == "0"):
                ThirdP = int(Data[IndexNumber + 3])
            else:
                ThirdP = IndexNumber + 3

            if (int(FirstP) < int(SecondP)):
                Data[ThirdP] = 1
            else:
                Data[ThirdP] = 0
            IndexNumber += 4

        elif (OpCode == "08"):
            FirstP = SecondP = ThirdP = 0
            if (FullCode[2] == "0"):
                FirstP = Data[int(Data[IndexNumber + 1])]
            else:
                FirstP = Data[IndexNumber + 1]

            if (FullCode[1] == "0"):
                SecondP = Data[int(Data[IndexNumber + 2])]
            else:
                SecondP = Data[IndexNumber + 2]

            if (FullCode[0] == "0"):
                ThirdP = int(Data[IndexNumber + 3])
            else:
                ThirdP = IndexNumber + 3

            if (int(FirstP) == int(SecondP)):
                Data[ThirdP] = 1
            else:
                Data[ThirdP] = 0
            IndexNumber += 4
        elif (OpCode == "99"):
           # print("exited successfully ")
            if(systemIndex == 4):
                global ended
                ended = True
                #print(str(systemIndex+1)+". module has ended ")
                break
                endedCircuit = True
                return0
            else:
                return 0
        else:
            #print("something's wrong, i can feel it")
            break
    return 0

curMax = 0
for i in range(len(allPossibleCombinations)):
    ended = False

    inputArr = []
    dataArr = []

    indexArr=[]
    for k in range(5):
        inputArr.append([])
        inputArr[k].append(allPossibleCombinations[i][k])

        dataArr.append([])
        dataArr[k] = DataOriginal.copy()

        indexArr.append(0)

    #first input 0
    inputArr[0].append(0)
    lastEoutput=0
    while(not ended):

        output = Circuit(0)
        inputArr[1].append(output)
        if(ended):
            break
        output = Circuit(1)
        inputArr[2].append(output)
        if (ended):
            break
        output = Circuit(2)
        inputArr[3].append(output)
        if (ended):
            break
        output = Circuit(3)
        inputArr[4].append(output)
        if (ended):
            break
        output = Circuit(4)
        if(output != 0):
            lastEoutput= output
        inputArr[0].append(output)
        if (ended):
            break
    print(lastEoutput,curMax)
    if (int(lastEoutput) >int(curMax)):
        curMax = int(lastEoutput)


print(curMax)

