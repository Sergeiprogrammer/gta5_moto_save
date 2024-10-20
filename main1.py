import time
from PIL import ImageGrab
import subprocess
from datetime import datetime

# Функция для отключения Wi-Fi
def disable_wifi():
    subprocess.call('netsh interface set interface name="Wi-Fi" admin=disable', shell=True)
    current_time = datetime.now()
    print(f"Wi-Fi отключён в {current_time.day} {current_time.hour}:{current_time.minute}:{current_time.second}")

# Функция для включения Wi-Fi
def enable_wifi():
    subprocess.call('netsh interface set interface name="Wi-Fi" admin=enable', shell=True)
    current_time = datetime.now()
    print(f"Wi-Fi отключён в {current_time.day} {current_time.hour}:{current_time.minute}:{current_time.second}")

value = 0
# Задержка для подготовки
time.sleep(4)
# Открываем файл и читаем содержимое
with open("setup.txt", "r") as file:
    content = file.read().strip()  # Удаляем лишние пробелы и переносы строк

# Преобразуем содержимое в кортеж
bbox = tuple(map(int, content.split(',')))  # Разбиваем строку и конвертируем в числа

# Сделайте скриншот указанной области
screenshot = ImageGrab.grab(bbox=bbox)

# Список координат и ожидаемых цветов для проверки
coordinates_and_colors = [
    ((1623, 768), (71, 73, 72)),
    ((1649, 779), (205, 205, 207)),
    ((1659, 798), (6, 7, 6))
]

# Функция для получения цвета пикселя на определенной координате
def get_pixel_color(screenshot, x, y, bbox):
    # Координаты относительно изображения
    relative_x = x - bbox[0]
    relative_y = y - bbox[1]

    # Проверка, что координаты находятся внутри изображения
    width, height = screenshot.size
    if 0 <= relative_x < width and 0 <= relative_y < height:
        return screenshot.getpixel((relative_x, relative_y))
    else:
        raise ValueError(f"Координаты ({x}, {y}) выходят за пределы изображения.")

# Проверяем цвета для каждой координаты
for (x, y), expected_color in coordinates_and_colors:
    try:
        pixel_color = get_pixel_color(screenshot, x, y, bbox)
        if pixel_color == expected_color:
            value += 1
        else:
            print(f"Цвет пикселя на координатах ({x}, {y}) не совпадает: {pixel_color}, ожидалось: {expected_color}")
    except ValueError as e:
        print(e)
if value >= 3:
    disable_wifi()
    time.sleep(5)
    enable_wifi()
    value = 0
else:
    pass
