import cv2 as cv
from PIL import Image

fgbg = cv.createBackgroundSubtractorMOG2()

def detect(frame):
    # Apply background subtraction
    fgmask = fgbg.apply(frame)
    
    _,th=cv.threshold(fgmask,200,255,cv.THRESH_BINARY)
    # Apply thresholding to remove noise
    
    # Find contours of objects
    contours, hierarchy = cv.findContours(th, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Loop through detected objects
    for contour in contours:
        # Calculate area of object
        area = cv.contourArea(contour)
        # Filter out small objects
        if area > 3000:
            # Get bounding box coordinates
            x, y, w, h = cv.boundingRect(contour)
            shp=frame.shape[0]
            cv.putText(frame,"motion detected",(int(shp)-140,20),fontFace=cv.FONT_HERSHEY_COMPLEX,fontScale=1.0,color=(0,255,0),thickness=2)
            # Draw bounding box around object
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    
    return frame