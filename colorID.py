
import cv2
import numpy as np

frameHeight = 480
frameWidth = 640
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)


def empty(a):
    pass


cv2.namedWindow("HSV Window")
cv2.resizeWindow("HSV Window", 560, 480)
cv2.createTrackbar("h_min", "HSV Window", 0, 179, empty)
cv2.createTrackbar("h_max", "HSV Window", 179, 179, empty)
cv2.createTrackbar("s_min", "HSV Window", 0, 225, empty)
cv2.createTrackbar("s_max", "HSV Window", 225, 225, empty)
cv2.createTrackbar("v_min", "HSV Window", 0, 225, empty)
cv2.createTrackbar("v_max", "HSV Window", 225, 225, empty)

while True:
    _, img = cap.read()
    cv2.imread('img', cv2.IMREAD_ANYDEPTH)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("h_min", "HSV Window")
    h_max = cv2.getTrackbarPos("h_max", "HSV Window")
    s_min = cv2.getTrackbarPos("s_min", "HSV Window")
    s_max = cv2.getTrackbarPos("s_max", "HSV Window")
    v_min = cv2.getTrackbarPos("v_min", "HSV Window")
    v_max = cv2.getTrackbarPos("v_max", "HSV Window")
    print(h_min)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, v_max, s_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    Hstack = np.hstack([img, mask, result])

    cv2.imshow('color testing', Hstack)
    if cv2.waitKey(1) == 1 & 0xff == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
