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
    # Пути к двум изображениям
    image_path1 = "images/test1.jpg"
    image_path2 = "images/iTrapm.png"

    # Целевые размеры изображений
    target_width = 800
    target_height = 600

    # Загрузка изображений
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Масштабирование изображений
    resized_image1 = resize_image(image1, target_width, target_height)
    resized_image2 = resize_image(image2, target_width, target_height)

    # Отображение измененных изображений
    cv2.imshow("Resized Image 1", resized_image1)
    cv2.imshow("Resized Image 2", resized_image2)
    cv2.imwrite("ResizedImage1.png", resized_image1)
    cv2.imwrite("ResizedImage2.png", resized_image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
