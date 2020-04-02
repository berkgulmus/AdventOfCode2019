import math
import itertools
import copy

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def x(coordinates,pairs,velocities,simulNumb,periods,orgCord):
    step=0
    while (True):

        # applying gravity
        for i in pairs:
            if (coordinates[i[0]][simulNumb] < coordinates[i[1]][simulNumb]):
                velocities[i[0]][simulNumb] += 1
                velocities[i[1]][simulNumb] -= 1
            elif (coordinates[i[0]][simulNumb] > coordinates[i[1]][simulNumb]):
                velocities[i[0]][simulNumb] -= 1
                velocities[i[1]][simulNumb] += 1
            else:
                continue

        # moving the planes
        for i in range(len(coordinates)):
            coordinates[i][simulNumb] += velocities[i][simulNumb]

        contFlag = False
        for i in range(len(coordinates)):
            if (coordinates[i][simulNumb] != orgCord[i][simulNumb]):
                contFlag = True
                break
        if (not contFlag):
            periods.append(step + 2)
            break

        step += 1

    # if(step%10000==0):
    # print(step)




pairs = (list(itertools.combinations([0,1,2,3],2)))
data = open("Day12_Data.txt").readlines()
coordinates =[]
velocities =[]
for i in range(len(data)):
    coordinates.append(list(map(int,data[i].strip("\n").split(","))))
    velocities.append([])
    for j in range(3):
        velocities[i].append(0)

orgCord = copy.deepcopy(coordinates)
oldStates = []
matchOldState = False
step=0
simulNumb =0
periods =[]

x(coordinates,pairs,velocities,simulNumb,periods,orgCord)
simulNumb=1
x(coordinates,pairs,velocities,simulNumb,periods,orgCord)
simulNumb=2
x(coordinates,pairs,velocities,simulNumb,periods,orgCord)

answer = lcm(periods[0],periods[1])
answer= lcm(answer,periods[2])
print(answer)