import pytesseract
import cv2
import re
from PIL import Image, ImageFilter
import pymorphy2 
import inspect
import numpy
import imutils
from background_expansion import add_border
from cutPhoto import cut
from imgSize import resize_image


image_path = "original_images/image.png"

image = cv2.imread(image_path)

# Добавление границы к изображению
bordered_image = add_border(image)
cv2.imwrite(f"converted_photo/imageFon.png", bordered_image)

cropped_image = cut("converted_photo/imageFon.png")
cv2.imwrite(f"finally_photo/imageFinally.png", cropped_image)

    # Масштабирование изображения
resized_image = resize_image("finally_photo/imageFinally.png")

# Отображение измененного изображения
cv2.imshow("Resized Image", resized_image)
cv2.imwrite(f"result/imageResult.png", resized_image)
cv2.waitKey(0)

