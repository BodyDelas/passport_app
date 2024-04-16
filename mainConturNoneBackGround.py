import cv2
import imutils
import numpy as np

# Чтение изображения
image = cv2.imread("images/imageTramp.png")
original = image.copy()

# Преобразование в оттенки серого и размытие
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (1, 1), 0)

# Выделение краев
edges = cv2.Canny(gray, 10, 250)

# Закрытие контуров для улучшения их формы
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Нахождение контуров
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# Создание маски и вырезание объектов без фона
mask = np.zeros_like(gray)
for c in cnts:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02*p, True)
    if len(approx) == 4:
        cv2.drawContours(mask, [approx], -1, (255, 255, 255), -1)

# Применение маски к исходному изображению
result = cv2.bitwise_and(original, original, mask=mask)

# Отображение результата
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
