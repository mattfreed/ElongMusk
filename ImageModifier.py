

#First step is to detect Elons body
#Second step is to extract that from the image into a new image
#Now have 2 images, original and only elon
#Fill all elon in with pixel color to the left
#Get middle of Elon and extend pixels at theat level about 25%
#Combine the 2 images again for final image


import requests
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# url = 'https://imageproxy.themaven.net/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fmaven-user-photos%2Fmishtalk%2Feconomics%2FzmfATcSa4EegwR7v_znq6Q%2F_RCltvRIYUuIBSHeTVJs2g?w=684&q=40&h=412.0935350756534&auto=format&fit=crop&crop=focalpoint&fp-x=0.5&fp-y=0.5&fp-z=1&fp-debug=false'
# response = requests.get(url, stream = True)
image = cv2.imread('https___s3-us-west-2.amazonaws.jpg')
cv2.imshow('elon',image)
cv2.waitKey(0)
