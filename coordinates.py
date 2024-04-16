import cv2

def resize_image(image, target_width, target_height):
    # Получаем текущие размеры изображения
    height, width = image.shape[:2]

    # Вычисляем коэффициенты масштабирования для изменения размера изображения
    width_ratio = target_width / width
    height_ratio = target_height / height

    # Выбираем минимальный коэффициент, чтобы сохранить пропорции изображения
    min_ratio = min(width_ratio, height_ratio)

    # Размеры, к которым мы будем масштабировать изображение
    resized_width = int(width * min_ratio)
    resized_height = int(height * min_ratio)

    # Масштабируем изображение
    resized_image = cv2.resize(image, (resized_width, resized_height))

    return resized_image

def main():
    # Путь к изображению паспорта
    image_path = "images/imageTramp.png"

    # Целевые размеры изображения
    target_width = 800
    target_height = 600

    # Загрузка изображения
    image = cv2.imread(image_path)

    # Масштабирование изображения
    resized_image = resize_image(image, target_width, target_height)

    # Отображение измененного изображения
    cv2.imshow("test", resized_image)
    cv2.imwrite("test1.png", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
