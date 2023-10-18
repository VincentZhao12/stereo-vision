import numpy as np
import cv2

cap_left = cv2.VideoCapture(0)   
cap_right = cv2.VideoCapture(0)   
  
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out_left = cv2.VideoWriter('output_left.mov', fourcc, 20.0, (1920, 1080)) 
out_right = cv2.VideoWriter('output_right.mov', fourcc, 20.0, (1920, 1080)) 
  
while(True): 
    ret, frame = cap_left.read()  
    ret2, frame2 = cap_right.read() 
    
    print(cap_left.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap_left.get(cv2.CAP_PROP_FRAME_HEIGHT))
  
    if ret:
        out_left.write(frame) 
        cv2.imshow('Original_l', frame)  
    if ret2:
        # out_right.write(frame2)
        cv2.imshow('Original_r', frame2)   
      
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# Close the window / Release webcam 
cap_left.release() 
  
# After we release our webcam, we also release the output 
out_left.release()  
out_right.release()  
  
# De-allocate any associated memory usage  
cv2.destroyAllWindows() 