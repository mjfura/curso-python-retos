def sumatoria_mejorada():
    is_finished=False
    suma=0
    while not is_finished:
        input_num=input("Ingrese un numero: ")
        if not input_num.isnumeric():
            return print("Ingrese un número válido")
        num=float(input_num)
        suma+=num
        if(num==0):
            is_finished=True
    print(f"La sumatoria es: {suma}")
        