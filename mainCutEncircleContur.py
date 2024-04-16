import numpy
import cv2
import imutils


image = cv2.imread ("test3.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

edges = cv2.Canny(gray, 10, 200)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 100))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*p, True)
    if len(approx) == 4:
        # Получаем ограничивающий прямоугольник для контура
        x, y, w, h = cv2.boundingRect(approx)
        # Вырезаем область изображения по ограничивающему прямоугольнику
        cropped_image = image[y:y+h, x:x+w]
        # Отображаем вырезанную область
        cv2.imshow('Cropped Image', cropped_image)
        cv2.waitKey(0)