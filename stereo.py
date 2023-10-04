import cv2
import numpy as np
from matplotlib import pyplot as plt 

cap = cv2.VideoCapture("stereo2.mp4")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

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

  if ret:
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    left = frame[0:int(height), 0:int(width/2)]
    right = frame[0:int(height), int(width/2):int(width)]

    # simplifyFrame(left)

    stereo = cv2.StereoSGBM.create(
      minDisparity=2,
      numDisparities=32
    )

    
    disparity = stereo.compute(left,right)

    # disparity = cv2.blur(disparity,(20,20))
    disparity = cv2.medianBlur(disparity,5)

    colormap = plt.get_cmap('plasma')
    heatmap = (colormap(disparity) * 2**16).astype(np.uint16)[:,:,:3]
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_RGB2BGR)


    cv2.imshow('left',left)
    cv2.imshow('right',right)
    cv2.imshow('res',disparity / 256)
 
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break
 
cap.release()
cv2.destroyAllWindows()