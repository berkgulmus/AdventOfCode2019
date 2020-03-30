Data = open("Day8_Data.txt").read()
Data = Data.strip()
map_object = map(int,Data)
Data= list(map_object)


curMin = 9999999
winningLayer = -1
print(len(Data))
for i in range (int(len(Data) / 150 )):
    howManyZeros =0
    for j in range (150):
        if (Data[i*150+j] ==0):
            howManyZeros +=1
    if(howManyZeros < curMin):
        curMin = howManyZeros
        winningLayer = i
        print(str(winningLayer) + ". layer contains "+str(howManyZeros)  + " zeros")

countOfOnes = countOfTwos =0
for i in range (150):
    #print(Data[winningLayer+i])
    if(Data[winningLayer*150+i]== 1):
        countOfOnes+=1
    elif (Data[winningLayer*150 + i] == 2):
        countOfTwos += 1

print(countOfOnes,countOfTwos)
print(countOfOnes*countOfTwos)