import webbrowser as browser
import pyautogui as autogui
import time

#Hora do estudo:
def abrir_ead_faculdade():
    url = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    usuario = 'xxxxxxx'
    senha = 'xxxxx'

    browser.open(url)

    autogui.press('tab')
    autogui.write(usuario)
    autogui.press('tab')
    autogui.write(senha)
    autogui.press('enter')

abrir_ead_faculdade()