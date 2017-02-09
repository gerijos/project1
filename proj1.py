from PIL import Image
import os.path


#path to directory containing images
path = "/home/ubuntu/workspace/Project1/Project1Images"

#Creates an image list
imgList = [] 

for i in range(9):
    imgList.append(Image.open("Project1Images/" + str(i+1) + ".png")))

#makePicture creates a picture object

imgList = Image.open('')

#########
#nested loop that goes through each row and coloum of each image
for x in range(0,width):
    for y in range(0,height):
        redPixel = []
        greenPixel = []
        bluePixel = []
        
        #for loop to access pixels of each image
        for i in range(0,9):
            #"append" puts together each pixel
            redPixel.append(getRed(getPixel(pics[i],x,y)))
            greenPixel.append(getGreen(getPixel(pics[i],x,y)))
            bluePixel.append(getBlue(getPixel(pics[i],x,y)))
            
            #list is sorted for a list with an odd number of items -> middle value is "median"
            redPixel = sorted(redPixel)
            greenPixel = sorted(greenPixel)
            bluePixel = sorted(bluePixel)
            
            #assigns the empty pixels to newImage
            newImagePixel = getPixel(newImagePixel,x,y)
            
            #median equation -> where position m is equal to the number of pictures (9) -> index starts at 0
            m = ((9+1)/2)
            
            #assigns the RGB pixels value from RGBPixel[4] -> expression towards set
            setRed(newImagePixel,redPixel[m])
            setGreen(newImaePixel,greenPixel[m])
            setBlue(newImaePixel,greenPixel[m])
            
            #shows new image with the person removed
            show(newImaePixel)
############            

#new image to put average pixels -> this gives the dimensions equal to that of the pixels of the image(matrix)
newImageGrayScale = emptyImage(width,height)

for x in range(0, height):
    redPixel = []
    greenPixel = []
    bluePixel = []
    
    for i in range(0,9)
        redPixel.append(getRed(getPixel(pics[i],x,y))
        greenPixel.append(getGreen(getPixel(pics[i],x,y)))
        bluePixel.append(getBlue(getPixel(pics[i],x,y)))
        
        redPixel = sorted(redPixel)
        greenPixel = sorted(greenPixel)
        bluePixel = sorted(greenPixel)
        
        m = ((9+1)/2)
        
        redPixel =