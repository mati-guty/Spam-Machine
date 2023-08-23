import pyautogui
import webbrowser
from time import sleep

# include your country code and no spaces
phone = '+56977498038'

# open whatsapp web
webbrowser.open(f'https://web.whatsapp.com/send?phone={phone}')
sleep(5)

# open a simple file
with open('note.txt', 'r') as file:
    # iterate
    for line in file:
        # write the lines on page opened
        pyautogui.typewrite(line)

        # press enter (send message)
        pyautogui.press("enter")
