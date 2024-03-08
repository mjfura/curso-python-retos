from .validador_numero import convert_num
def sumatoria_series():
    is_finished_series=False
    suma_total=0
    while not is_finished_series:
        input_num_1=input("Ingrese el primer numero: ")
        num_1=convert_num(input_num_1)
        if not num_1:
            print("El numero ingresado no es valido")
            continue
        input_num_2=input("Ingrese el segundo numero: ")
        num_2=convert_num(input_num_2)
        if not num_2:
            print("El numero ingresado no es valido")
            continue
        suma=num_1+num_2
        print(f"La suma es: {suma}")
        if suma==0:
            is_finished_series=True
        suma_total+=suma
    print(f"La suma total es: {suma_total}")
    