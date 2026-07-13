#  traffic light 

import cv2
import numpy as np

img = np.zeros((500,500,3),dtype=np.uint8)

cv2.rectangle(img,(199,99),(299,299), (255,255,255), 5)
cv2.circle(img,(249,149),20,(0,0,255),cv2.FILLED)
cv2.circle(img,(249,199),20,(0,255,255),-1)
cv2.circle(img,(249,249),20,(0,255,0),-1)
cv2.imshow("Traffic Light", img)
cv2.waitKey(0)
cv2.destroyAllWindows()