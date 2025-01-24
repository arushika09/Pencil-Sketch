import cv2
import numpy as np

#taking the user input for the image file path
image_path = input("Enter the path to your image file: ")

#load the image
image = cv2.imread(image_path)

#check if the image is loaded sucessfully
if image is None:
    print("ERROR: Unable to load the image.")
else:
    #converting the image to grayscale
    gray_iamge=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #invert the grayscale image/negative image 
    inverted_gray_image= 255-gray_iamge

    #creating a blurred version of the inverted grayscale image
    blurred_image=cv2.GaussianBlur(inverted_gray_image,(21,21),0) 

    #now blend the grayscale image and blurred image to create a pencil sketch
    pencil_sketch= cv2.divide(gray_iamge,blurred_image, scale=256.0)

    # final creation: display the original image and the pencil sketch
    cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Original Image",image)
    # set the window size to image size
    cv2.resizeWindow('Original Image', image.shape[1], image.shape[0])

    cv2.namedWindow("Pencil Sketch", cv2.WINDOW_NORMAL)
    cv2.imshow("Pencil Sketch",pencil_sketch)
    cv2.resizeWindow('Pencil Sketch', pencil_sketch.shape[1], pencil_sketch.shape[0])

    cv2.waitKey(0)
    cv2.destroyAllWindows()

