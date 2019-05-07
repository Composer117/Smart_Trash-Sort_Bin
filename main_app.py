import time
import calendar
import datetime
import camera
import motion
import os
from classify_image import run_inference_on_image
from class_list import class_dictionary
from camera import Camera

waste_type = {"r":"Recycling", "c":"Compost"}

class_dictionary = class_dictionary()

def predict_top_5(image_url):
    print("Tensorflow is processing the image...")
    return run_inference_on_image(image_url)

def top_prediction_name(prediction):
    return prediction[4]

def what_is_it(image_name):
    top_5 = predict_top_5(image_name)  # Pulling-out the top 5 matched results
    print(top_5)

    top = top_5[4]  # Pulling-out the top class
    top_name = top[0]  # Pulling-out the top class name

    print("THE OBJECT WAS: " + top_name)

    if class_dictionary[top_name] == 'c':
#<<<<<<< HEAD

#=======
#>>>>>>> abb619bc169ab5fe281bc988c2bdb0b6c04768ca
        return 'c'
    else:
        return 'r'

def sort_trash(imgpath):
    camera1 = Camera()  
    # No movement detected
    while True:
        print("\nWaiting for motion.....")
        motion.waitForMotionDetection()
        time.sleep(0.125)

        print("Detected motion!!")
        
        camera1.takePhoto(imgpath)
        print("Image of intrusion captured")
        trash_type = what_is_it(imgpath)
        print("WASTE TYPE: " + waste_type[trash_type])
        


def main():
    sort_trash('/home/pi/Desktop/Capstone_Project/f_code/FinalPic/classificationImage.jpg')

if __name__ == '__main__':
    main()