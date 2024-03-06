

def sumatoria():
    print('Ingresar un número N: ')
    input_n=input()
    if not input_n.isdigit():
        return print('Debe ingresar un número entero')
    n=int(input_n)
    suma=0
    print('La cantidad de números que debe ingresar es :',n)
    while(n>0):
        print('Ingrese un número: ')
        input_num=input()
        if not input_num.isnumeric():
            return print('Debe ingresar un número')
        num=int(input_num)
        suma+=num
        n-=1
    return print('La suma es: ',suma)