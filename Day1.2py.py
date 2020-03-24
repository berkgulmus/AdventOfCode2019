
Total_Fuel_Need =0
Data_File = open("Day1_Data.txt")

Data_Lines = Data_File.readlines()

for i in range(len(Data_Lines)):
    Data_Lines[i] = int(Data_Lines[i].rstrip('\n'))
    Module_Fuel_Need = int(Data_Lines[i] / 3) - 2
    Fuel_Fuel_Need= Module_Fuel_Need
    Total_Fuel_Need+= Module_Fuel_Need
    #print(Module_Fuel_Need)
    while(True):
        Fuel_Fuel_Need = int(Fuel_Fuel_Need / 3) - 2
        if(Fuel_Fuel_Need <=0 ):
            break
        else:
            Total_Fuel_Need += Fuel_Fuel_Need
            #print(Fuel_Fuel_Need)

print(Total_Fuel_Need)

