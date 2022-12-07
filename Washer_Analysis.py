import cv2
import numpy as np

img = cv2.imread('Images/badw.jpg')
cv2.imshow("Input Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,80,200,0)

cv2.imshow("Thresholded Washer", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((2,2), np.uint8)
c = cv2.erode(thresh, kernel, iterations=75)

contours,hierarchy = cv2.findContours(c, 1, 2)
cnt = contours[0]
print(cnt)
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
print("Area = ",area)
perimeter = cv2.arcLength(cnt,True)
print("Perimeter = ",perimeter)
pi = 22/7;
circ = (4*pi*area)/(perimeter**2)
print("Circularity = ",circ)

circstr = str(circ)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(c,'Circularity : '+ circstr,(10,50), font, 1,(255,255,255),2)
cv2.imshow("Eroded Washer", c)
cv2.waitKey(0)
cv2.destroyAllWindows()



if 0.4 <= circ <=0.69 :
    cv2.putText(img,'Bad Washer',(200,100), font, 2,(255,255,255),3)  
    cv2.imshow("Washer Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
elif 0.7 <= circ <=1.0 :
    cv2.putText(img,'Good Washer',(200,100), font, 2,(255,255,255),3)  
    cv2.imshow("Washer Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    cv2.putText(img,'Invalid Object',(200,100), font, 2,(255,255,255),3)  
    cv2.imshow("Washer Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()