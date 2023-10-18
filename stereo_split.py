import cv2
import numpy as np
from matplotlib import pyplot as plt 

cap = cv2.VideoCapture("stereo2.mp4")
# leftCap = cv2.VideoCapture("left.webm")
# rightCap = cv2.VideoCapture("right.webm")

# object_detector = cv2.createBackgroundSubtractorMOG2()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow("res")

cv2.createTrackbar("min disparities", "res", 1, 128, lambda x: print(x))
cv2.setTrackbarPos("min disparities", "res", 1)
cv2.createTrackbar("num disparities", "res", 1, 256, lambda x: print(x))
cv2.setTrackbarPos("num disparities", "res", 16)
cv2.createTrackbar("block size", "res", 1, 256, lambda x: print(x))
cv2.setTrackbarPos("block size", "res", 20)
cv2.createTrackbar("p1", "res", 1, 1000, lambda x: print(x))
cv2.setTrackbarPos("p1", "res", 330)
cv2.createTrackbar("p2", "res", 1, 1000, lambda x: print(x))
cv2.setTrackbarPos("p2", "res", 0)

cv2.createTrackbar("speckle range", "res", 1, 1000, lambda x: print(x))
cv2.setTrackbarPos("speckle range", "res", 0)

cv2.createTrackbar("speckle size", "res", 1, 1000, lambda x: print(x))
cv2.setTrackbarPos("speckle size", "res", 0)

cv2.createTrackbar("unique", "res", 1, 20, lambda x: print(x))
cv2.setTrackbarPos("unique", "res", 0)



# def simplifyFrame(frame):
#   r = 0
#   l = 0
  
#   while r < len(frame):
#     row  = frame[r]
#     l = 0
#     # print(r)
#     while l < len(row):
#       subframe = frame[r:min(len(frame), r + 16), l:min(len(row), l + 16)]
#       print(str(int(subframe.mean())) + " ", end="")
#       l+=16
#     print("")
#     r+=16

# def compute(left, right):



while(cap.isOpened()):
# if True:
  ret, frame = cap.read()
#   ret, left = leftCap.read();
#   ret2, right = rightCap.read();

  if ret:

    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    # right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

    left = frame[0:int(height), 0:int(width/2)]
    right = frame[0:int(height), int(width/2):int(width)]

    # mask = object_detector.apply(left)


    left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

    # simplifyFrame(left)

    stereo = cv2.StereoSGBM.create(
      minDisparity=cv2.getTrackbarPos("min disparities", "res"), 
      numDisparities=cv2.getTrackbarPos("num disparities", "res"), 
      blockSize=cv2.getTrackbarPos("block size", "res"), 
      P1=cv2.getTrackbarPos("p1", "res"), 
      P2=cv2.getTrackbarPos("p2", "res"), 
      disp12MaxDiff=0, 
      preFilterCap=0, 
      uniquenessRatio=cv2.getTrackbarPos("unique", "res"), 
      speckleWindowSize=cv2.getTrackbarPos("speckle size", "res"), 
      speckleRange=cv2.getTrackbarPos("speckle range", "res")
    )

    
    disparity = stereo.compute(left,right)

    disparity = cv2.blur(disparity,(20,20))
    disparity = cv2.medianBlur(disparity,5)

    colormap = plt.get_cmap('plasma')
    heatmap = (colormap(disparity) * 2**16).astype(np.uint16)[:,:,:3]
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)


    cv2.imshow('left',left)
    cv2.imshow('right',right)
    # cv2.imshow('mask',mask)
    cv2.imshow('res', disparity)
 
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break
 
cap.release()
cv2.destroyAllWindows()