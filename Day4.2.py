

def getNumb(Arr):
    return 100000*Arr[0]+10000*Arr[1]+1000*Arr[2]+100*Arr[3]+10*Arr[4]+Arr[5]

rangeStart = 367479
rangeFinish =893698

Array=[]
Array.append(3)
Array.append(6)
Array.append(7)
Array.append(4)
Array.append(7)
Array.append(9)


Lim=[]
Lim.append(8)
Lim.append(9)
Lim.append(3)
Lim.append(6)
Lim.append(9)
Lim.append(8)
Results=[]

for x0 in range(Array[0],Lim[0]+1,1):
    Array[0] = x0
    for x1 in range(x0,10,1):
        Array[1] = x1
        for x2 in range(x1, 10, 1):
            Array[2] = x2
            for x3 in range(x2, 10, 1):
                Array[3] = x3
                for x4 in range(x3, 10, 1):
                    Array[4] = x4
                    for x5 in range(x4, 10, 1):
                        Array[5] = x5
                        HaveOnly2Multiples = False
                        for i in range(5):
                            if(Array[i]==Array[i+1]):
                                Temporary = True
                                if(i != 0  ):
                                    if(Array[i-1]== Array[i]):
                                        Temporary=False
                                if(i != 4 ):
                                    if(Array[i]==Array[i+2]):
                                        Temporary = False
                                if(Temporary):
                                    HaveOnly2Multiples = True

                        if(HaveOnly2Multiples ):
                            numb = getNumb(Array)
                            if(numb >= rangeStart and numb <= rangeFinish):
                                Results.append(numb)

print(Results)
print(len(Results))