import time
from datetime import datetime
import subprocess
from io import BytesIO
from PIL import Image

#Temporary Image Folder filepath
temp = "/home/pi/Desktop/Capstone_Project/f_code/TempPic"   
threshold = 15
sensitivity = 800

def capture():
    filepath = temp + "/test.jpg"
    subprocess.call('fswebcam -r 1280x960 --jpeg 95 -q --save {}'.format(filepath), shell=True)
    img = Image.open(filepath)
    return img

def convert2Stream(image):
    b = BytesIO()
    image.save(b,"JPEG")
    return b
 
def captureTestImage():
    stream = BytesIO()
    img = capture()
    stream = convert2Stream(img)
    stream.seek(0)
    image = Image.open(stream)
    buffer = image.load()
    stream.close()
    return image, buffer

def waitForMotionDetection():
    # Get first image
    image1, buffer1 = captureTestImage()

    while (True):
        # Get comparison image
        image2, buffer2 = captureTestImage()

        # Count changed pixels
        changedPixels = 0
        for x in range(0, 1280):
            for y in range(0, 960):
                # Just check green channel - it's highest quality
                pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
                if pixdiff > threshold:
                    changedPixels += 1
                    
        # Break out of the loop if the pixels have changed
        if changedPixels > sensitivity:
            break

        # Swap comparison buffers
        image1 = image2
        buffer1 = buffer2

        # Wait for half a second before taking another picture
        time.sleep(0.0625)

