def get_line_intersection( p0_x,  p0_y,  p1_x,  p1_y,
     p2_x,  p2_y,  p3_x,  p3_y):


    s1_x = p1_x - p0_x
    s1_y = p1_y - p0_y
    s2_x = p3_x - p2_x
    s2_y = p3_y - p2_y

    if((-s2_x * s1_y + s1_x * s2_y) == 0):
        return 0,0
    else:
        s = (-s1_y * (p0_x - p2_x) + s1_x * (p0_y - p2_y)) / (-s2_x * s1_y + s1_x * s2_y)
        t = ( s2_x * (p0_y - p2_y) - s2_y * (p0_x - p2_x)) / (-s2_x * s1_y + s1_x * s2_y)

        if (s >= 0 and s <= 1 and t >= 0 and t <= 1):
            i_x = p0_x + (t * s1_x)
            i_y = p0_y + (t * s1_y)
            return i_x,i_y;


    return 0,0







Data_File = open("Day3_Data.txt")
Data = Data_File.readlines()

Data_A = Data[0].split(',')
Data_B = Data[1].split(',')

Points_A = []
Points_B = []

Coordinate_X = Coordinate_Y = 0

for i in range(len(Data_A)):
    direction = Data_A[i][:1]
    length = int(Data_A[i][1:])
    if(direction == 'U'):
        Coordinate_Y+= length
    elif(direction == 'D'):
        Coordinate_Y -= length
    elif(direction == 'R'):
        Coordinate_X += length
    elif(direction == 'L'):
        Coordinate_X-=length
    Points_A.append([Coordinate_X,Coordinate_Y])

Coordinate_Y=Coordinate_X = 0
for i in range(len(Data_B)):
    direction = Data_B[i][:1]
    length = int(Data_B[i][1:])
    if(direction == 'U'):
        Coordinate_Y+= length
    elif(direction == 'D'):
        Coordinate_Y -= length
    elif(direction == 'R'):
        Coordinate_X += length
    elif(direction == 'L'):
        Coordinate_X-=length
    Points_B.append([Coordinate_X,Coordinate_Y])

minimumValue = 999999999
for i in range(len(Points_A)-1):
    for k in range(len(Points_B)-1):
        """Intersection_X = False
        if( Points_A[i][0] <=  Points_B[k][0] and Points_A[i+1][0] >= Points_B[k][0]):
            Intersection_X = True
        elif(Points_A[i][0] >=  Points_B[k][0] and Points_A[i+1][0] <= Points_B[k][0]):
            Intersection_X = True
        elif (Points_A[i][0] <= Points_B[k+1][0] and Points_A[i + 1][0] >= Points_B[k+1][0]):
            Intersection_X = True

        elif (Points_A[i][0] >= Points_B[k+1][0] and Points_A[i + 1][0] <= Points_B[k+1][0]):
            Intersection_X = True

        Intersection_Y = False
        if (Points_A[i][1] <= Points_B[k][1] and Points_A[i + 1][1] >= Points_B[k][1]):
            Intersection_Y = True
        elif (Points_A[i][1] >= Points_B[k][1] and Points_A[i + 1][1] <= Points_B[k][1]):
            Intersection_Y = True
        elif (Points_A[i][1] <= Points_B[k + 1][1] and Points_A[i + 1][1] >= Points_B[k + 1][1]):
            Intersection_Y = True
        elif (Points_A[i][1] >= Points_B[k + 1][1] and Points_A[i + 1][1] <= Points_B[k + 1][1]):
            Intersection_Y = True

        if(Intersection_X == True  and Intersection_Y == True):
            print("found intersection   " + str(Points_A[i]) + str(Points_A[i+1 ])+ str(Points_B[k]) + str(Points_B[k+1]))
        
        """
        resultX, resultY = get_line_intersection(Points_A[i][0],Points_A[i][1],Points_A[i+1][0],Points_A[i+1][1],Points_B[k][0],Points_B[k][1],Points_B[k+1][0],Points_B[k+1][1])

        if (resultX != 0 and resultY !=0):
            print("intersection found  " + str(resultX) +"  " + str(resultY))
            if((int.__abs__(int(resultX)) + int.__abs__(int(resultY))) < minimumValue):
                minimumValue = int.__abs__(int(resultX)) + int.__abs__(int(resultY))
print((minimumValue))