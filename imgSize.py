import cv2

def resize_image(image):
    # Целевые размеры изображения
    target_width = 415
    target_height = 600

    # Масштабирование изображения
    resized_image = cv2.resize(image, (target_width, target_height))

    return resized_image

def main():
    # Путь к изображению паспорта
    image_path = "images/test1.jpg"

    # Загрузка изображения
    image = cv2.imread(image_path)

    # Масштабирование изображения
    resized_image = resize_image(image)

    # Отображение измененного изображения
    cv2.imshow("Resized Image", resized_image)
    cv2.imwrite("test3.png", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
