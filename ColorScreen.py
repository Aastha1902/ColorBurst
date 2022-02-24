
import cv2
import numpy as np

frameHeight = 480
frameWidth = 640
myColors = [[155, 84, 0, 179, 224, 225],  # red
            [80, 110, 113, 101, 158, 225],  # green
            [104, 127, 130, 179, 225, 225],  # blue
            [106, 104, 136, 179, 203, 181]]  # purple

myColorValues = [[0, 0, 200],
                 [0, 200, 0],
                 [200, 0, 0],
                 [50, 0, 100]]

myPoints = []  # [x, y, colorId]


def FindColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 4, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
    # cv2.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.001 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y


def drawOnCanvas(myPOints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 4, myColorValues[point[2]], cv2.FILLED)

cap = cv2.VideoCapture(0)
cap.set(25, frameWidth)
cap.set(5, frameHeight)
cap.set(10, 150)
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = FindColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("result", imgResult)
    if cv2.waitKey(1) == 1 & 0xff == ord('a'):
        break
