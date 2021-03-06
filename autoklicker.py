import keyboard
from time import sleep
import threading


def get_key():
    moeglichkeiten = "123456"
    rueckgabe = {"1": "up", "2":"down", "3":"left", "4":"right", "5":"e", "6":"tab"}

    print("Bitte Taste auswählen")
    print("1 = up")
    print("2 = down")
    print("3 = left")
    print("4 = right")
    print("5 = e")
    print("6 = tab")

    ui = input("Bitte ein Zahl von 1-6 eingeben: ") 
    if ui not in moeglichkeiten:
        print("nur Zahlen von 1-6 eingeben", end='')
        exit(0)

    return rueckgabe[ui]

def get_time():
    time = input("Wie lange soll die Pause in Sekunden sein?\nPause: ")

    try:
        time =  float(time)
    except: 
        print("nur Zahlen eingeben", end='')
        exit(0)
    
    if time < 0:
            print("Nur Positive Zahlen eingeben", end='')
            exit(0)
    return time


def loop(key, time):
    keyboard.send(key)
    sleep(time)

if __name__ == "__main__":
    key = get_key()
    time = get_time()

    start_key = 66 # F8
    on = False
    print("F8 drücken um zu starten")
    x = threading.Thread(target=loop,args=(key,time) , daemon=True)


    while True:
        sleep(.001)
        if keyboard.is_pressed(start_key) and not on:
            print("Schleife an")
            on = True
            while keyboard.is_pressed(start_key):
                sleep(.1)

        if keyboard.is_pressed(start_key) and on:
            print("Schleife aus")
            on = False
            while keyboard.is_pressed(start_key):
                sleep(.1)

        if not x.is_alive() and on:
            x = threading.Thread(target=loop,args=(key,time) , daemon=True)
            x.start()
        

