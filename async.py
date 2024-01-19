import threading
import os
import keyboard

def x():
    p = 0
    while 5 > 0:
        print('p') #Repetição

def y():
    while True:
        if keyboard.is_pressed('k'): #Para o programa ao apertar K
            os._exit(0)
                
threading.Thread(target=x).start() #Roda as funções ao mesmo tempo
threading.Thread(target=y).start()
threading.Thread(target=p).start()