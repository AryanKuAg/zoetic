import pyscreenshot as ImageGrab
import pyautogui
from PIL import ImageGrab
import keyboard
while True:
    try:
        if keyboard.is_pressed('p'):
            image = ImageGrab.grab()
            image.save("screenshot.png")
            break
        else:
            pass
    except:
        break


# Get the XY position of the mouse.
# currentMouseX, currentMouseY = pyautogui.position()

# print(currentMouseX, currentMouseY)

# print(pyautogui)

# # part of the screen
# im = ImageGrab.grab(bbox=(10, 10, 500, 500))
# im.show()

# # to file
# ImageGrab.grab_to_file('im.png')
