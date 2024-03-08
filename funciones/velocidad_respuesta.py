import random
import time
def imprimir_aleatorio(message:str,max):
    segundos=random.randint(1,max)
    time.sleep(segundos)
    print(message)
def carrera():
    imprimir_aleatorio('Preparados',3)
    imprimir_aleatorio('Listos', 3)
    imprimir_aleatorio('Ya', 5)
    inicio=time.time()
    n=input("Presione enter")
    fin=time.time()
    print(f"Tiempo de respuesta: {fin-inicio}")