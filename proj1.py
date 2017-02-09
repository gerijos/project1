from PIL import Image

#path to directory containing images
pics = Image.open("./Project1Images/1.png")
pics = Image.open("./Project1Images/2.png")
pics = Image.open("./Project1Images/3.png")
pics = Image.open("./Project1Images/4.png")
pics = Image.open("./Project1Images/5.png")
pics = Image.open("./Project1Images/6.png")
pics = Image.open("./Project1Images/7.png")
pics = Image.open("./Project1Images/8.png")
pics = Image.open("./Project1Images/9.png")

def medianOdd(imageList):
    median = 0
    #store list length in the variable listLength
    listLength = len(imageList)
    #sort the list
    sortedValues = sorted(imageList)
    #Location of middle value. Substract one because of zero index
    sortedValues = sorted(imageList)
    middleIndex = ((listLength + 1)/2)-1
    #return the object located that index
    return sortedValues[middleIndex]

#Creates an image list
imList = [] 

#to get the width and height of an image
width = imList[0].size
height = imList[1].size

redPixel = []
greenPixel = []
bluePixel = []

myRed, myGreen, myBlue = imList[6].getpixel((2,3))

print(myRed, myGreen, myBlue)

#creates new image with the given mode and size -> size is a 2-tuble ordered list
imageNew = (Image.new('RGB',width, height, 'white'))

#nested for loop that goes across each column and row
for x in range (0,width):
    for y in range(0,height):
        #for loop to access pixels of each image
        for i in range(0,9):
            redPixel.append(getmyRed(getpixel(pics[i](x,y)))
            greenPixel.append(getmyGreen(myImage.getpixel((x,y)))
            bluePixel.append(getmyBlue(myImage.getpixel((x,y)))
           
            
        
        
        
            
            
            
            