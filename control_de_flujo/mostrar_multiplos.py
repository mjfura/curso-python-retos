from typing import List
def mostrar_multiplos(numeros:List[int],inicio:int, limite:int):
    for i in range(inicio,limite+1):
        size=len(numeros)
        contador=0
        for numero in numeros:
            if i % numero == 0:
                contador+=1
        if size == contador:
            print(f"{i} es múltiplo")