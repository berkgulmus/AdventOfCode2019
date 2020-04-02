import itertools

pairs = (list(itertools.combinations([0,1,2,3],2)))
data = open("Day12_Data.txt").readlines()
coordinates =[]
velocities =[]
for i in range(len(data)):
    coordinates.append(list(map(int,data[i].strip("\n").split(","))))
    velocities.append([])
    for j in range(3):
        velocities[i].append(0)


step = 0
while(step != 1000):

    #applying gravity
    for i in pairs:
        for j in range(3):#for 3 coordinates
            if(coordinates[i[0]][j] < coordinates[i[1]][j]):
                velocities[i[0]][j] +=1
                velocities[i[1]][j] -= 1
            elif(coordinates[i[0]][j] > coordinates[i[1]][j]):
                velocities[i[0]][j] -=1
                velocities[i[1]][j] += 1
            else:
                continue

    #moving the planes
    for i in range(len(coordinates)):
        for j in range(3):
            coordinates[i][j]+=velocities[i][j]

    step +=1

totalEnergy =0
for i in range(len(coordinates)):
    temp1 =temp2=0
    for j in range(3):
        temp1 += abs(coordinates[i][j])
        temp2 += abs(velocities[i][j])
    totalEnergy += temp1*temp2
print(totalEnergy)