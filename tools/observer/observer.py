import pyautogui
import base64
from PIL import Image
import io

screenshot =  pyautogui.screenshot()

scale_factor = 0.8
new_width = int(screenshot.width * scale_factor)
new_heght = int(screenshot.height * scale_factor)

compressed_image = screenshot.resize((new_width, new_heght))

image_buffer = io.BytesIO()
compressed_image.save(image_buffer, format='PNG')
compressed_image_bytes = image_buffer.getvalue()
base64_str = base64.b64encode(compressed_image_bytes).decode('utf-8')

with open("scr.txt", "w") as file:
    file.write(base64_str)

with open("scr.png", 'wb') as file:
    file.write(base64.b64decode(base64_str))