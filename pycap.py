import pyautogui
import os

os.environ['DISPLAY'] = ':0'


pyautogui.screenshot('./test.png', region=(0, 0, 1920, 1080))