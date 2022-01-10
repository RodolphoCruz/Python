import pyautogui as auto
import threading
import keyboard
import time

rodar = True

def normal():
    global rodar
    
    comando = {"atualizar" : (120,75), "entrar" : (957,803), "metamask" : (1806,693), "tesouro" : (954,566), "herois" : (954,923), "work" : (847,398), "fechar" : (1023,337), "voltar" : (405, 232)}
    
    def atualizar():
        if rodar:
            auto.click(comando["atualizar"])
            time.sleep(10)
        if rodar:
            auto.click(comando["entrar"])
            time.sleep(20)
        if rodar:
            auto.click(comando["metamask"])
            tempo = time.localtime()
            t = time.strftime("%H:%M:%S", tempo)
            print("Atualizou: {}".format(t))
            time.sleep(30)
    
    def trabalhar():
        if rodar:
            auto.click(comando["tesouro"])
            time.sleep(10)
        if rodar:
            auto.click(comando["herois"])
            time.sleep(10)
        if rodar:
            auto.click(comando["herois"])
            time.sleep(10)
        if rodar:
            auto.click(comando["work"])
            time.sleep(10)
        if rodar:
            auto.click(comando["fechar"])
            time.sleep(5)
        if rodar:
            auto.click(comando["fechar"])
            tempo = time.localtime()
            t = time.strftime("%H:%M:%S", tempo)
            print("Trabalhar: {}".format(t))
            time.sleep(5)
            auto.click(comando["fechar"])

    def reorganizar():
        if rodar:
            print("voltar")
            auto.click(comando["voltar"])
            tempo = time.localtime()
            t = time.strftime("%H:%M:%S", tempo)
            print("Reorganizar: {}".format(t))
            time.sleep(5)
    

    while rodar:
        atualizar()
        trabalhar()
        time.sleep(600)
        reorganizar()
        trabalhar()
        time.sleep(600)
        reorganizar()
        trabalhar()
        time.sleep(600)
        



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


