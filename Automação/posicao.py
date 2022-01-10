import pyautogui as auto
import keyboard
import threading

rodar = True

def posicao():
    global rodar
    while rodar:
        keyboard.wait('m')
        x, y = auto.position()
        print('{} , {}'.format(x,y))
        print('----------')

def get_input():
    global rodar
    print('Precione q depois m para sair')
    keyboard.wait('q')
    print('Você saiu do programa')
    rodar=False

n=threading.Thread(target=posicao)
i=threading.Thread(target=get_input)
n.start()
i.start()
