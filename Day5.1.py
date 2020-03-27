Data_File = open("Day5_Data.txt")
Data = Data_File.read()
Data = Data.split(',')
#for i in range(len(Data)):
   # Data[i]=int(Data[i])



IndexNumber =0

while(True):
    TempLen = len(str(Data[IndexNumber]))
    StringToAdd = ""
    for i in range(5-TempLen):
        StringToAdd += "0"
    Data[IndexNumber] = StringToAdd+str(Data[IndexNumber])
    FullCode = str(Data[IndexNumber])
    OpCode= Data[IndexNumber][-2:]
    if(OpCode== "01"):
        NumbToAdd1=NumbToAdd2=0
        if(FullCode[2]=="0"):
            NumbToAdd1 = Data[int(Data[IndexNumber+1])]
        else:
            NumbToAdd1 = Data[IndexNumber + 1]

        if (FullCode[1] == "0"):
            NumbToAdd2 = Data[int(Data[IndexNumber + 2])]
        else:
            NumbToAdd2 = Data[IndexNumber + 2]
        if(FullCode[0] == "0"):
            PlaceToWrite =int(Data[IndexNumber+3])
        else:
            PlaceToWrite= IndexNumber+3
        Data[PlaceToWrite] = int(NumbToAdd1)+int(NumbToAdd2)
        IndexNumber+=4
    elif(OpCode=="02"):
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

        IndexNumber +=4
    elif(OpCode=="03"):
        userinput = 1

        if (FullCode[2] == "0"):
            PlaceToWrite = int(Data[IndexNumber + 1])
        else:
            PlaceToWrite = IndexNumber + 1

        Data[PlaceToWrite]= int(userinput)
        IndexNumber+=2
    elif(OpCode=="04"):
        NumbToWrite =0
        if(FullCode[2]=="0"):
            NumbToWrite=Data[int(Data[IndexNumber + 1])]
        else:
            NumbToWrite=int(Data[IndexNumber+1])
        print(NumbToWrite)
        IndexNumber+=2

    elif(OpCode=="99"):
        print("exited successfully")
        exit()
    else:
        print("something's wrong, i can feel it")
        break



