
Total_Fuel_Need =0

Data_File = open("Day1_Data.txt")

Data_Lines = Data_File.readlines()

for i in range(len(Data_Lines)):
    Data_Lines[i] = int(Data_Lines[i].rstrip('\n'))
    Total_Fuel_Need += int(Data_Lines[i] / 3) - 2

print(Total_Fuel_Need)

