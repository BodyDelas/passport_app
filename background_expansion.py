import cv2
import numpy as np

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
