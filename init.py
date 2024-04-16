import pytesseract
import cv2
import re
from PIL import Image, ImageFilter
import pymorphy2 
import inspect
import numpy
import imutils
from utils import *



image_path = "original_images/image.png"
image = cv2.imread(image_path)

# Добавление границы к изображению
bordered_image = add_border(image)
cv2.imwrite(f"converted_photo/imageFon.png", bordered_image)


cropped_image = cut("converted_photo/imageFon.png")
cv2.imwrite(f"finally_photo/imageFinally.png", cropped_image)


 # Масштабирование изображения
resized_image = resize_image("finally_photo/imageFinally.png")
cv2.imwrite(f"result/imageResult.png", resized_image)

name = cutName("result/imageResult.png")
print(f"Имя: {name}")

second_name = cutSecondName("result/imageResult.png")
print(f"фамилия: {second_name}")

therdName = cutTherdName("result/imageResult.png")
print(f"Отчество: {therdName}")

gender = cutGender("result/imageResult.png")
print(f"Гендер: {gender}")

cutCity("result/imageResult.png")

birth = cutDateBirth("result/imageResult.png")
print(f"Дата рождения: {birth[0]}")

Ser_and_Num(image_path)

code(image_path)

extradition = cutDateExtradition("result/imageResult.png")
print(f"Дата выдачи: {extradition[0]}")

cutPassportExtradition("result/imageResult.png")


# Отображение измененного изображения
cv2.imshow("Resized Image", resized_image)
cv2.imwrite(f"result/imageResult.png", resized_image)
cv2.waitKey(0)

