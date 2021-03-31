#Healthy Programmer
from datetime import datetime
from time import time
from pygame import mixer

def audio_play(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input=input("Enter codeword to stop the music\t").upper()
        if user_input==stopper:
            mixer.music.stop()
            break

def Log_book(message):
    with open("MY_logbook.txt","a") as file:
        file.write(f"{message} {datetime.now()}\n")


if __name__ == '__main__':
    init_water = time()
    init_eyes =time()
    init_physical =time()
    water_drinking_gap=10
    Eyes_rest_gap=100
    Physica_exe_gap=150
    while True:
        if time()-init_water>water_drinking_gap:
            print("Water Exercise!! Write 'Done' to stop")
            audio_play("Scam1992.mp3","DONE")
            init_water=time()
            Log_book("Water Exercise Done At")

        if time()-init_eyes>Eyes_rest_gap:
            print("Eyes Exercise!! Write 'Done' to stop")
            audio_play("Scam1992.mp3","DONE")
            init_eyes=time()
            Log_book("Eyes Exercise Done At")

        if time()-init_physical>Physica_exe_gap:
            print("physical Exercise!! Write 'Done' to stop")
            audio_play("Scam1992.mp3","DONE")
            init_physical=time()
            Log_book("Physical Exercise Done At")