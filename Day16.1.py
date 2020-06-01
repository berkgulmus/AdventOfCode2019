import time
def getMultiplier(repeatVal, pos):
    index = int((pos+1)/repeatVal)%4
    #pos+1 because we have to shift the array 1 value to the left
    # int(x/repeat) because we will repeat each element in repeating pattern repeatVal times
    # %4 is because of original repeatin pattern length

    return repeatingPattern[index]

def FFT(inputSignal):
    #we enter inputSignal as a list of values


    outputSignal =[]

    for i in range(len(inputSignal)):
        output=0
        for iter,element in enumerate(inputSignal):
           # timeBfMult = time.perf_counter()
            multiplier = getMultiplier(i+1, iter)
            #timeAfMult = time.perf_counter()
            if(multiplier ==0):
                continue
            else:
                output += element*multiplier

        output = abs(output)%10
        outputSignal.append(output)
    return outputSignal

#creating an array of numbers
dataString= "59791875142707344554745984624833270124746225787022156176259864082972613206097260696475359886661459314067969858521185244807128606896674972341093111690401527976891268108040443281821862422244152800144859031661510297789792278726877676645835805097902853584093615895099152578276185267316851163313487136731134073054989870018294373731775466754420075119913101001966739563592696702233028356328979384389178001923889641041703308599918672055860556825287836987992883550004999016194930620165247185883506733712391462975446192414198344745434022955974228926237100271949068464343172968939069550036969073411905889066207300644632441054836725463178144030305115977951503567"
dataInt =[]
for char in dataString:
    dataInt.append(int(char))


repeatingPattern=[0,1,0,-1]

counter =0

while(counter!=100):
    #timeBfFTT=time.perf_counter()
    dataInt = FFT(dataInt)
    #timeAfFTT = time.perf_counter()
    counter+=1
    #print("time elapsed :" + str(timeAfFTT-timeBfFTT))
print(dataInt)
