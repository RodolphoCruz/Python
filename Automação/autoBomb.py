import pyautogui as auto
import threading
import keyboard
import time

rodar = True

def normal():
    global rodar
    
    comando = {"atualizar" : (120,75), "entrar" : (957,803), "metamask" : (1806,693), "tesouro" : (954,566), "herois" : (954,923), "work" : (849,402), "fechar" : (1023,337), "voltar" : (405, 232)}
    
    def esperar(t):
        t = t
        while rodar and t:
            time.sleep(1)
            t -= 1
    
    def atualizar():
        if rodar:
            auto.moveTo(comando["atualizar"])
            time.sleep(0.25)
            auto.click()
            time.sleep(10)
        if rodar:
            auto.moveTo(comando["entrar"])
            time.sleep(0.25)
            auto.click()
            time.sleep(20)
        if rodar:
            auto.moveTo(comando["metamask"])
            time.sleep(0.25)
            auto.click()
            tempo = time.localtime()
            t = time.strftime("%H:%M:%S", tempo)
            print("Atualizou: {}".format(t))
            time.sleep(25)
    
    def trabalhar():
        if rodar:
            auto.moveTo(comando["tesouro"])
            time.sleep(0.25)
            auto.click()
            time.sleep(5)
        if rodar:
            auto.moveTo(comando["herois"])
            time.sleep(0.25)
            auto.click()
            time.sleep(2)
            auto.click()
            time.sleep(10)
        if rodar:
            auto.moveTo(comando["work"])
            time.sleep(0.25)
            auto.click()
            time.sleep(10)
        if rodar:
            auto.moveTo(comando["fechar"])
            time.sleep(0.25)
            auto.click()
            time.sleep(2)
            auto.click()
            time.sleep(1)
        if rodar:
            tempo = time.localtime()
            t = time.strftime("%H:%M:%S", tempo)
            print("Trabalhar: {}".format(t))

    def reorganizar():
        if rodar:
            auto.moveTo(comando["voltar"])
            time.sleep(0.25)
            auto.click()
            time.sleep(1)
        if rodar:
            tempo = time.localtime()
            t = time.strftime("%H:%M:%S", tempo)
            print("Reorganizar: {}".format(t))    

    while rodar:
        atualizar()
        trabalhar()
        esperar(600)
        reorganizar()
        trabalhar()
        esperar(600)
        reorganizar()
        trabalhar()
        esperar(600)
        



def get_input():
    global rodar
    print('Precione q para sair')
    keyboard.wait('q')
    print('Você saiu do programa')
    rodar=False

n=threading.Thread(target=normal)
i=threading.Thread(target=get_input)
time.sleep(10)
n.start()
i.start()


