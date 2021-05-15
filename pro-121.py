import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')

outputfile = cv2.VideoWriter('pro-4cc.avi',fourcc,20,(640,480))

capture = cv2.VideoCapture(0)

time.sleep(3)

bg = 0

for i in range (0,60):
  ret,bg = capture.read()

while (capture.isOpened()):
  ret,image = capture.read()
  if(not ret):
    break
  hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
  lower_red = np.array([0,120,50])
  upper_red = np.array([10,255,255])
  mask_1 = cv2.inRange(hsv,lower_red,upper_red)
  lower_red_2 = np.array([170,120,70])
  upper_red_2 = np.array([180,255,255])
  mask_2 = cv2.inRange(hsv,lower_red_2,upper_red_2)
  mask_1 = mask_1 + mask_2
  mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
  mask_1 = cv2.morphologyEx(mask_1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
  mask_2 = cv2.bitwise_not(mask_1)
  res = cv2.bitwise_and(image,image,mask = mask_2)
  res1 = cv2.bitwise_and(bg,bg,mask = mask_1)
  finaloutput = cv2.addWeighted(res,1,res1,1,0)
  outputfile.write(finaloutput)
  cv2.imshow("image1",finaloutput)
  cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()