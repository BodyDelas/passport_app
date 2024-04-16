import cv2
import numpy as np
import imutils
import pytesseract
import re


def add_border(image):
    # Получаем текущие размеры изображения
    height, width = image.shape[:2]

    # Увеличиваем размеры изображения на 300 пикселей с каждой стороны
    new_height = height + 600  # 300 пикселей сверху и снизу
    new_width = width + 600    # 300 пикселей слева и справа

    # Создаем новое изображение с увеличенным размером и заполняем его белым цветом
    border_color = (255, 255, 255)  # Белый цвет
    bordered_image = np.full((new_height, new_width, 3), border_color, dtype=np.uint8)

    # Вычисляем координаты для вставки оригинального изображения
    y_offset = 300  # Смещение по вертикали
    x_offset = 300  # Смещение по горизонтали

    # Вставляем оригинальное изображение внутрь нового изображения
    bordered_image[y_offset:y_offset+height, x_offset:x_offset+width] = image
    return bordered_image


def cut(puth):
    image = cv2.imread (puth)
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

    cropped_image = cv2.GaussianBlur(cropped_image, (1, 1), 0)
    return cropped_image


def resize_image(image):
    # Целевые размеры изображения
    image = cv2.imread(image)
    target_width = 415
    target_height = 600

    # Масштабирование изображения
    resized_image = cv2.resize(image, (target_width, target_height))
    return resized_image


def cutSecondName(puti):
# Загрузка изображения
    image = cv2.imread(puti)

    # Координаты верхнего левого угла области для обрезки (x, y)
    x = 150
    y = 320

    # Ширина и высота области для обрезки
    width = 220
    height = 30

    # Обрезка изображения по указанным координатам и размерам
    cropped_image = image[y:y+height, x:x+width]

    # Сохранение обрезанного изображения
    # cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.search(r'[А-Я]+', text)
    if match:
        substring = match.group(0)
    return substring


def cutName(puti):

    image = cv2.imread(puti)

    x = 150
    y = 365

    width = 220
    height = 30

    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.search(r'[А-Я]+', text)
    if match:
        substring = match.group(0)
    return substring


def cutTherdName(puti):

    image = cv2.imread(puti)

    x = 150
    y = 390

    width = 220
    height = 30

    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.search(r'[А-Я]+', text)
    if match:
        substring = match.group(0)
    return substring


def cutGender(puti):

    image = cv2.imread(puti)

    x = 130
    y = 410

    width = 220
    height = 30

    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.search(r'[А-Я]+', text)
    if match:
        substring = match.group(0)
    return substring


def cutDateBirth(puti):

    image = cv2.imread(puti)

    x = 130
    y = 410

    width = 220
    height = 30

    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)

    return match


def cutDateExtradition(puti):

    image = cv2.imread(puti)

    x = 35
    y = 120

    width = 220
    height = 30

    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.findall(r'\d{2}\.\d{2}\.\d{4}', text)

    return match 


def cutCity(puti):

    image = cv2.imread(puti)

    x = 130
    y = 435

    width = 220
    height = 30

    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.findall(r'[А-Я]+', text)

    print(f"Место рождения: {match[0]} {match[1]}")


def cutPassportExtradition(puti):

    image = cv2.imread(puti)

    x = 60
    y = 45

    width = 300
    height = 85

    cropped_image = image[y:y+height, x:x+width]

    cv2.imwrite("test.png", cropped_image)

    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(cropped_image, config=config)
    match = re.findall(r'[А-Я]+', text)
    
    temp = ' '.join(match)

    print(f"Паспорт выдан: {temp}")


def Ser_and_Num(puti):
    img = cv2.imread(puti)
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


def code(puti):
    img = cv2.imread(puti)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    config = r'--oem 3 --psm 6 -l rus'
    text = pytesseract.image_to_string(img, config=config)
    sequence = re.search(r'\d{3}-\d{3}', text)

    print(f"Код подразделения: {sequence[0]}")
