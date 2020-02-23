import cv2
import numpy as np

for i in range(1,6): 
 img=cv2.imread('C:\Python\coba.png',1)
 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#[[20, 100, 100], [40, 255, 255] – Kuning
 lower_api1 = np.array([20, 100, 100])
 upper_api1 = np.array([40, 255, 255])
 mask1 = cv2.inRange(hsv, lower_api1, upper_api1)

 mask = mask1

 new_img = cv2.bitwise_and(img, img, mask=mask)
 
 
 cv2.imshow("Hasil"+str(i)+".png",new_img)
 cv2.imshow('image', img)
 

#menunggu tombol key ditekan
 cv2.waitKey(0)
 cv2.destroyAllWindows()
