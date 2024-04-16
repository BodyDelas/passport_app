import cv2

def resize_image(image):
    # Целевые размеры изображения
    image = cv2.imread(image)
    target_width = 415
    target_height = 600

    # Масштабирование изображения
    resized_image = cv2.resize(image, (target_width, target_height))

    return resized_image
