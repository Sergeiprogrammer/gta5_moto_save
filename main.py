from pynput.mouse import Listener
import pyautogui
from PIL import ImageGrab

coordinates = []

print("кликни на правый верхний и левый нижний угол правай кнопкой мыши а координаты запиши в txt файл")
def on_click(x, y, button, pressed):
    if button.name == 'right' and pressed:
        if len(coordinates) != 4:
            current_position = pyautogui.position()
            print(f"{current_position.x}, {current_position.y}")
            coordinates.append(current_position.x)
            coordinates.append(current_position.y)
            screenshot = ImageGrab.grab()
            color = screenshot.getpixel((current_position.x, current_position.y))
        else:
            print("впишите это в txt файл")
            print(f"bbox = ({coordinates[0]}, {coordinates[1]}, {coordinates[2]}, {coordinates[3]})")
            bbox = (coordinates[0], coordinates[1], coordinates[2], coordinates[3])
            text_to_write = f"{coordinates[0]}, {coordinates[1]}, {coordinates[2]}, {coordinates[3]}"

            # Открываем файл для записи (если файл не существует, он будет создан)
            with open("setup.txt", "w") as file:
                # Записываем строку в файл
                file.write(text_to_write)
            # Сделайте скриншот указанной области
            screenshot = ImageGrab.grab(bbox=bbox)

            # Сохраните или обработайте скриншот, например, сохраните его в файл
            screenshot.save("screen.png")
            print("выключите программу и посмотрите точно ли вы определили облость проверки! в папке появился файл screen.png")



# Запускаем мониторинг мыши
with Listener(on_click=on_click) as listener:
    listener.join()
