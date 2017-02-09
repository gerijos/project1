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
            
            
            
from PIL import Image
import os.path

#path to directory containing images
path = "/home/ubuntu/workspace/Project1/Project1Images"

#Creates an image list
imgList = [] 

for i in range(9):
    imgList.append(Image.opne("Project1Images/" + str(i+1) + ".png")))

#makePicture creates a picture object

imgList = Image.open('')