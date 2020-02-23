import cv2
import numpy as np

for i in range(1,7): 
 img=cv2.imread('C:\Python\coba5.png',1)
 hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 lower_biru = np.array([0, 0, 0], dtype=np.uint8)
 upper_biru = np.array([255, 255, 150], dtype=np.uint8)

 #[0, 0, 0], [255, 255, 150] – Hitam
 mask1 = cv2.inRange(hsv, lower_biru, upper_biru)
 mask = mask1
 new_img = cv2.bitwise_and(img, img, mask=mask)
 cv2.imshow('mask',mask)
 cv2.imshow('image', img)
#menunggu tombol key ditekan
 cv2.waitKey(0)
