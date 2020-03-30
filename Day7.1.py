from itertools import permutations

Data_File = open("Day7_Data.txt")
DataOriginal = Data_File.read()
DataOriginal = DataOriginal.split(',')
#for i in range(len(Data)):
   # Data[i]=int(Data[i])

Numbers = [ 0,1,2,3,4]

allPossibleCombinations = list(permutations(Numbers,r=5))
currentMost = 0
currentWinningOrder =[]
def Circuit(Data,phase,input):
    IndexNumber = 0
    inputCounter =0
    Inputs=[]
    Inputs.append(phase)
    Inputs.append(input)
    while (True):
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
            userinput = Inputs[inputCounter]
            inputCounter+=1

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
            return  NumbToWrite
            IndexNumber += 2

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
            print("exited successfully")
            exit()
        else:
            print("something's wrong, i can feel it")
            break
    return 0


for i in range(len(allPossibleCombinations)):
    inputVal =0
    DataCopy = DataOriginal.copy()
    for j in range(len(allPossibleCombinations[i])):
        inputVal=Circuit(DataCopy,allPossibleCombinations[i][j],inputVal)
    if(inputVal>currentMost):
        currentWinningOrder= list(allPossibleCombinations[i]).copy()
        currentMost = inputVal
        print(str(currentWinningOrder) + "     "+str(inputVal))


print(currentWinningOrder)
