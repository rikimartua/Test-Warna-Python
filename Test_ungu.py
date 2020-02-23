import cv2
import numpy as np

for i in range(1,6): 
 img=cv2.imread('C:\Python\coba2.png',1)
 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#[150, 100, 100], [165, 255, 255] – Ungu
 lower_api1 = np.array([120, 100, 100])
 upper_api1 = np.array([140, 255, 255])
 mask1 = cv2.inRange(hsv, lower_api1, upper_api1)

 mask = mask1

 new_img = cv2.bitwise_and(img, img, mask=mask)
 
 
 cv2.imshow("Hasil"+str(i)+".png",new_img)
 cv2.imshow('image', img)
 

#menunggu tombol key ditekan
 cv2.waitKey(0)
 cv2.destroyAllWindows()
