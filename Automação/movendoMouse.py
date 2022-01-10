import pyautogui
import time

comando = {"atualizar" : (114,77), "entrar" : (940,823) }

time.sleep(2)
pyautogui.moveTo(comando["atualizar"])
time.sleep(2)
pyautogui.moveTo(comando["entrar"])
