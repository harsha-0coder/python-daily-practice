# text on image with condition 

import cv2
import numpy as np

mode = input("Enter the mode: ").lower()
battery = int(input("Enter the battery value: "))
x = 100
y =50


img = np.zeros((800,800,3),dtype=np.uint8)
cv2.putText(img, f"Battery ={battery} %",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
cv2.putText(img,"Altitude: 1 M",(x,y+50),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
cv2.putText(img,"FPS : 30", (x,y+100), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
if mode == "guided" :
      cv2.putText(img,f"Mode: {mode}",(x,y+150),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

else:
      cv2.putText(img,f"Mode: {mode}",(x,y+150),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow("Dashboard", img)
cv2.waitKey(0)
cv2.destroyAllWindows()