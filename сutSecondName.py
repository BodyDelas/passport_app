import cv2

# Загрузка изображения
image = cv2.imread("result/imageResult.png")

# Координаты верхнего левого угла области для обрезки (x, y)
x = 100
y = 50

# Ширина и высота области для обрезки
width = 300
height = 200

# Обрезка изображения по указанным координатам и размерам
cropped_image = image[y:y+height, x:x+width]

# Сохранение обрезанного изображения
cv2.imwrite("cropped_image.jpg", cropped_image)