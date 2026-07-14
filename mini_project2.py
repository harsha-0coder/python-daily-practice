# putting text on the image

import cv2
import numpy as np

img = np.zeros((1000,1000,3),dtype=np.uint8)
cv2.putText(img,"Name: Harsh",(100,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)
cv2.putText(img,"Course : Computer Vision",(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)
cv2.putText(img,"Module :4",(100,150),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),5)
cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()