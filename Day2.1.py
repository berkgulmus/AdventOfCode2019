Data_File = open("Day2_Data.txt")
Data = Data_File.read()
Data = Data.split(',')
for i in range(len(Data)):
    Data[i]=int(Data[i])



#"To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2."
Data[1]=int(12)
Data[2]=int(2)

Index_Number = 0
while(True):
    if(Data[Index_Number] == 1):
        Data[Data[Index_Number+3]] = Data[Data[Index_Number+1]] + Data[Data[Index_Number+2]]
        Index_Number +=4
    elif(Data[Index_Number] ==2):
        Data[Data[Index_Number + 3]] = Data[Data[Index_Number + 1]] * Data[Data[Index_Number + 2]]
        Index_Number += 4
    elif(Data[Index_Number] == 99):
        print("Terminated successfully")
        break
    else:
        print("Something has gone wrong, read opcode:"+Data[Index_Number])
        print("Terminated")
        break

print(Data[0])