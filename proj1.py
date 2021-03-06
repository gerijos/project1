from PIL import Image

img = []
#path to directory containing images
img.append(Image.open("./Project1Images/1.png"))
img.append(Image.open("./Project1Images/2.png"))
img.append(Image.open("./Project1Images/3.png"))
img.append(Image.open("./Project1Images/4.png"))
img.append(Image.open("./Project1Images/5.png"))
img.append(Image.open("./Project1Images/6.png"))
img.append(Image.open("./Project1Images/7.png"))
img.append(Image.open("./Project1Images/8.png"))
img.append(Image.open("./Project1Images/9.png"))


#to find the midian
def median(imageList):
    median = 0
    #Sorts the list 
    sortedList = sorted(imageList)
    #store list length in the variable lenghtlist
    lengthList = len(sortedList)
    #location of middle value
    centerIndex = lengthList/2
    if len(sortedList) == 1:
        for value in sortedList:
            median += value
        return median
    
#example provided by the teacher   
#store list length in the variable listLength
  #listLength = len(imageList)
    #sort the list
   # sortedValues = sorted(imageList)
    #Location of middle value. Substract one because of zero index
   # sortedValues = sorted(imageList)
   # middleIndex = ((listLength + 1)/2)-1
    #return the object located that index
  #  return sortedValues[middleIndex]
    
    #to find the median 
    elif len(sortedList) % 2 == 0:
        temp = 0.0
        medianparties = []
        medianparties = sortedList[centerIndex -1 : centerIndex + 1]
        for value in medianparties:
            temp += value
            median = temp /2
        return median
        
    else:
        middleIndex = []
        middleIndex = [sortedList[centerIndex]]
        for value in middleIndex:
            median = value
        return median
    
# this is the size of the picture
imgwidth,imgheight = img[0].size

newImage = Image.new("RGB",(imgwidth,imgheight),"white")

# the list and shades of colors of the picture
redPixel=[]
greenPixel=[]
bluePixel=[]

# x and y are the height and width of the pictures
for x in range(imgwidth):
     for y in range(imgheight):
        for i in img:
            myblue, mygreen, myred = i.getpixel((x,y))
            redPixel.append(myred)
            greenPixel.append(mygreen)
            bluePixel.append(myblue)

        medianRed = median(redPixel)
        medianGreen = median(greenPixel)# median of the pixelisted
        medianBlue = median(bluePixel)

        newImage.putpixel((x,y),(medianRed, medianGreen, medianBlue))

        redPixel =[]
        greenPixel =[]
        bluePixel = []

# the final picture        
newImage.save("final.png")


