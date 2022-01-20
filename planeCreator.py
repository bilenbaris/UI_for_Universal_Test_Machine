import cv2
import numpy as np

class PlanCreation():
    def __init__(self):
        pass
          
    def __findColor(self,frame, myColor):  # Color detection
        newPoints = []
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        lower = np.array(myColor[0:3])
        upper = np.array(myColor[3:6])
        mask = cv2.inRange(frameHSV, lower, upper)
        # cv2.imshow("Result", mask)
        midPoints = self.__getContours(mask)
        for points in midPoints:
            x,y = points[0], points[1]
            if (x != 0 and y != 0):
                newPoints.append([x, y])
        return newPoints

    def __getContours(self,frame):  # Contour fix
        midPoints = []
        contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                cv2.drawContours(frame, cnt, -1, (255, 255, 0), 3)
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                x, y, w, h = cv2.boundingRect(approx)
                midPoints.append([x+w//2, y+h//2])
        return midPoints

    def findPlaneMidPoint(self,frame,colour):
        midPoint = []
        colorAxis = self.__findColor(frame,colour)
        # print(colorAxis)
        length = len(colorAxis)
        midPointX = [p[0] for p in colorAxis]
        midPointY = [p[1] for p in colorAxis]
        if(length == 0):
            return midPoint
        midPoint = np.array([int(sum(midPointX)/length),int(sum(midPointY)/length)])
        print(midPoint)
        return midPoint