from multiple_imageprocessing import *
import numpy as np
import cv2
import matplotlib.pyplot as plt


######################################################
#               Process Frame
######################################################
def processFrame(frame):
    pf = preprocessing(frame)
    tagCoordinates = detectArTag(pf,frame)
    if(tagCoordinates is not None):
        desiredCoordinates =  np.float32([[0,0],[200,0],[0,200],[200,200]])
        
        tagstr = ""
        for i in range(len(tagCoordinates)):
            tag = orientation(tagCoordinates[i].copy())

            hmat = homography(tag,desiredCoordinates)
            warpedtag = cv2.warpPerspective(frame,hmat,(200,200))
            # warpedtag = warpFrame(frame,hmat,(200,200),tag)

            center = tuple((tag.sum(axis=0)/4 + np.array([30,30])).astype(int)) 
            print(center)
             
            tagId = retrieveInfo(warpedtag,1,i) 
            tagstr += "tag detected " + str(i) + "-" + ''.join(str(e) for e in tagId) + "\n  \n" 
            cv2.putText(frame,"tag " + str(i),center, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255),5)   


        for i, line in enumerate(tagstr.split('\n')):
                y = 300 + i*20
                cv2.putText(frame, line, (10, y ), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),3)   

        cv2.imshow('AR Tag using custom wrap function',frame)



######################################################
#              Reading Video 
#####################################################
cap = cv2.VideoCapture('./data/Video_dataset/multipleTags.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

    processFrame(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()






# dst = cv2.cornerHarris(fp,2,3,0.04)
# dst = cv2.dilate(dst,None,iterations=0)
# frame[dst>0.01 * dst.max()] =[0,255,0]

# dst = cv2.cornerHarris(gray,2,3,0.04)
# ratio = img.shape[0]/300
# img = cv2.imread('./data/reference_images/ref_marker.png')
# detectArTag(img)

# gray = np.float32(gray)
# canny = cv2.Canny(img,100,200)


# erode =cv2.erode(thresh,None, iterations=3)
# dilate = cv2.dilate(thresh,None,iterations=3)





