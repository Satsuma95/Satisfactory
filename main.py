import pyautogui
import time
path = r"C:\Users\User\AppData\Local\FactoryGame\Saved\SaveGames\76561199444955034\autosave_2"
time.sleep(3)
clickdropcords = pyautogui.locateOnScreen(image="clickdrop.PNG")
pyautogui.click(clickdropcords)
time.sleep(1)
pyautogui.write(path)
pyautogui.press("enter")
time.sleep(15)
statis = pyautogui.locateOnScreen(image="statictiks.PNG")
pyautogui.click(statis)
time.sleep(2)
water = pyautogui.locateOnScreen(image="water.PNG")
pyautogui.moveTo(water.left+water.width,water.top)
pyautogui.mouseDown()
pyautogui.moveRel(20,510)
pyautogui.scroll(-10000)



"""
- Сделать контрл+С
- загуглитоь: "как достать значения с буфера обмена на пайтоне", попробовать достать из буфера и просто опринтовать то, что ботяра скопировал)
"""
