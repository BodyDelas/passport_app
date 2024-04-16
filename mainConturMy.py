import numpy
import cv2
import imutils


image = cv2.imread ("images/test1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (1, 1), 0)

edges = cv2.Canny(gray, 10, 250)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

mask = numpy.zeros_like(gray)
total = 0
for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*p, True)
    if len(approx) == 4:
        total +=1
        cv2.drawContours(mask, [approx], -1, 255, -1)


# Применение маски к исходному изображению
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Result', result)
cv2.waitKey(0)