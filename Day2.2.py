Data_File = open("Day2_Data.txt")
Data = Data_File.read()
Data = Data.split(',')
for i in range(len(Data)):
    Data[i]=int(Data[i])
Data_Backup = Data.copy()



for noun in range (100):
    for verb in range(100):
        Data = Data_Backup.copy()
        Data[1] = noun
        Data[2] = verb
        Index_Number = 0
        while(True):
            if(Data[Index_Number] == 1):
                Data[Data[Index_Number+3]] = Data[Data[Index_Number+1]] + Data[Data[Index_Number+2]]
                Index_Number +=4
            elif(Data[Index_Number] ==2):
                Data[Data[Index_Number + 3]] = Data[Data[Index_Number + 1]] * Data[Data[Index_Number + 2]]
                Index_Number += 4
            elif(Data[Index_Number] == 99):
                #print("Terminated successfully")
                break
            else:
               #print("Something has gone wrong, read opcode:"+ str(Data[Index_Number]))
                #print("Terminated")
                break
        if(Data[0] == 19690720):
            print("noun :" + str(noun) )
            print("verb :" + str(verb) )
            exit()
