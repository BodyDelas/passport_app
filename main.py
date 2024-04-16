import pytesseract
import cv2
import re
from PIL import Image, ImageFilter
import pymorphy2 
import inspect


img = cv2.imread('images/image.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Поворот изображения на 90 градусов по часовой стрелке
rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

config = r'--oem 3 --psm 6 -l rus'
text_rotate = pytesseract.image_to_string(rotated_img, config=config)

# Регулярное выражение для поиска трех последовательных чисел
pattern = r'(\b\d+\b \b\d+\b \b\d+\b)'
# поиск всех совпадений
mas_Ser_and_Num = re.findall(pattern, text_rotate)

str_Ser_and_Num = mas_Ser_and_Num[0].replace(" ", "")

series = str_Ser_and_Num[:4]
number = str_Ser_and_Num[4:]

print(f"Серия: {series}")
print(f"Номер: {number}")

text = pytesseract.image_to_string(img, config=config)
print(text)
dates = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)
# print(dates)

print(f"Дата выдачи: {dates[0]}")
print(f"Дата рождения: {dates[1]}")

sequence = re.search(r'\d{3}-\d{3}', text)
print(f"Код подразделения: {sequence[0]}")


# uppercase_words = re.findall(r'\b[A-ZА-Я]+\b', text)
# print(uppercase_words)


cv2.imshow('Result', img)
cv2.waitKey(0)




