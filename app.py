import pyscreenshot as ImageGrab
import pyautogui
from PIL import ImageGrab
import keyboard
while True:
    try:
        if keyboard.is_pressed('`'):
            currentMouseX1, currentMouseY1 = pyautogui.position()
            currentMouseX2 = currentMouseX1 + 400
            currentMouseY2 = currentMouseY1 + 200
            # image.save("screenshot30.png")
            im = ImageGrab.grab(
                bbox=(currentMouseX1, currentMouseY1, currentMouseX2, currentMouseY2))
            im.save('screenshot.png')
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
