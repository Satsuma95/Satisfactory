import pyautogui
import time
import pyperclip
import telebot
from config import TOKENT

AXTUNG = telebot.TeleBot(TOKENT)
admin = 5414030971
@AXTUNG.message_handler(commands=['start'])
def start(message):
    AXTUNG.send_message(message.chat.id,"статы по сатисфактори")
    AXTUNG.send_sticker(message.chat.id, "CAACAgIAAxkBAAELaNtlzjbdEGTKv-xxVTTDWKuo5HiDRgACShsAAo9-CUkFx6SkNGB_jjQE")
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
    pyautogui.hotkey("ctrl","c")
    oleg = pyautogui.locateOnScreen(image="electro2.PNG")
    pyautogui.click(oleg)
    pyautogui.click(oleg)
    pyautogui.click(oleg)
    time.sleep(1)
    oleg2 = pyautogui.locateOnScreen(image="electro.PNG")
    pyautogui.click(oleg2)
    time.sleep(1)
    oleg3 = pyautogui.locateOnScreen(image="20.PNG")
    pyautogui.click(oleg3)
    time.sleep(1)
    screen = pyautogui.screenshot('power.png')
    print(screen)
    text = f"{pyperclip.paste()}"
    print (text)
    AXTUNG.send_message(message.from_user.id,text)
    AXTUNG.send_photo(message.from_user.id,screen)

AXTUNG.polling()


"""
- Сделать контрл+С
- загуглитоь: "как достать значения с буфера обмена на пайтоне", попробовать достать из буфера и просто опринтовать то, что ботяра скопировал)
"""


















