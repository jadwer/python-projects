# importa el modulo time
import time
from playsound import playsound

def countdown_timer(seconds):
    while seconds > 0:

        mins = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{mins}:{secs}'

        print(timer, end='\r') # \n\r 'Nueva linea' 'retorno de carro'
        time.sleep(1)

        seconds -= 1
    print('¡Se acabó el tiempo!')
    playsound('./mixkit-sound.wav')


#input time en segundos
seconds = input("Escribe el tiempo en segundos: ")
# Llama a la función
countdown_timer(int(seconds))

