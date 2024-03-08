def calcular_primo(n:int):
    contador=1
    contador_primos=0
    list_primos=[]
    while contador_primos<n:
        numero_divisores=0
        for i in range(1,contador+1):
            if contador%i==0:
                numero_divisores+=1
        if numero_divisores==2:
            contador_primos+=1
            list_primos.append(contador)
        contador+=1
    print(list_primos)