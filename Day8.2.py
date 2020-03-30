from PIL import Image
zoomX=zoomY = 10
im= Image.new('RGB', (25*zoomX,6*zoomY))


Data = open("Day8_Data.txt").read()
Data = Data.strip()
map_object = map(int,Data)
Data= list(map_object)

resultData =[]
curMin = 9999999
winningLayer = -1
print(len(Data))
for offset in range (150):
    tempVal =0
    while(True):
        if(Data[tempVal*150+offset]== 1 or Data[tempVal*150+offset]== 0):
            resultData.append(Data[tempVal*150+offset])
            break
        else:
            tempVal+=1


for pix in range(len(resultData)):
    pixX = pix%25
    pixY = int(pix/25)

    for xVal in range(zoomX):
        for yVal in range(zoomY):
            if(resultData[pix]==1):
                im.putpixel((pixX* zoomX + xVal, pixY*zoomY+yVal),(255,255,255,255) )
            elif(resultData[pix]==0):
                im.putpixel((pixX* zoomX + xVal, pixY*zoomY+yVal),(0,0,0,255) )

im.show()
im.save("result.jpg")
print(resultData)