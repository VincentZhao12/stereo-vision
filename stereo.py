import cv2
import numpy as np
from matplotlib import pyplot as plt 

# cap = cv2.VideoCapture("stereo2.mp4")
# leftCap = cv2.VideoCapture("left.webm")
# rightCap = cv2.VideoCapture("right.webm")
object_detector = cv2.createBackgroundSubtractorMOG2()

def show_stereo():

    stereo = cv2.StereoSGBM.create(
      minDisparity=4, 
      numDisparities=64, 
      blockSize=5, 
      P1=0, 
      P2=0, 
      disp12MaxDiff=0, 
      preFilterCap=0, 
      # uniquenessRatio=cv2.getTrackbarPos("unique", "res"), 
      # speckleWindowSize=cv2.getTrackbarPos("speckle size", "res"), 
      # speckleRange=cv2.getTrackbarPos("speckle range", "res")
    )

    
    disparity = stereo.compute(left,right)

    disparity = cv2.blur(disparity,(20,20))
    disparity = cv2.medianBlur(disparity,5)

    colormap = plt.get_cmap('plasma')
    heatmap = (colormap(disparity) * 2**16).astype(np.uint16)[:,:,:3]
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)


    cv2.imshow('left',left)
    cv2.imshow('right',right)
    cv2.imshow('res', disparity/256.0)
    # cv2.imshow('mask', mask_l)
 
    cv2.waitKey()

# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cv2.namedWindow("res")

cv2.createTrackbar("min disparities", "res", 1, 128, show_stereo)
cv2.setTrackbarPos("min disparities", "res", 1)
cv2.createTrackbar("num disparities", "res", 1, 256, show_stereo)
cv2.setTrackbarPos("num disparities", "res", 16)
cv2.createTrackbar("block size", "res", 1, 256, show_stereo)
cv2.setTrackbarPos("block size", "res", 20)
cv2.createTrackbar("p1", "res", 1, 1000, show_stereo)
cv2.setTrackbarPos("p1", "res", 330)
cv2.createTrackbar("p2", "res", 1, 1000, show_stereo)
cv2.setTrackbarPos("p2", "res", 0)

cv2.createTrackbar("speckle range", "res", 1, 1000, show_stereo)
cv2.setTrackbarPos("speckle range", "res", 0)

cv2.createTrackbar("speckle size", "res", 1, 1000, show_stereo)
cv2.setTrackbarPos("speckle size", "res", 0)

cv2.createTrackbar("unique", "res", 1, 20, show_stereo)
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


left = cv2.imread('calibresult1.png', 1)
right = cv2.imread('calibresult2.png', 1)

# while True:
# if True:
  # ret, frame = cap.read()
  # ret, left = leftCap.read();
  # ret2, right = rightCap.read();

  # if True:
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # left_unfiltered = left

    # mask_l = object_detector.apply(left)
    # mask_r = object_detector.apply(right)

    # left = cv2.bitwise_and(left, left, mask=mask_l)
    # right = cv2.bitwise_and(right, right, mask=mask_r)

left = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
right = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)

    # left = frame[0:int(height), 0:int(width/2)]
    # right = frame[0:int(height), int(width/2):int(width)]

    

    # simplifyFrame(left)
  
    
show_stereo()
 
leftCap.release()
rightCap.release()
cv2.destroyAllWindows()