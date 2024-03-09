import typing
'''
[
    {
        "name":"Función 1",
        "description":"Descripción de la función 1",
        "callback":función1
    }
]
'''
# DEFINIENDO TIPO PARA PARÁMETRO
FunctionItem=typing.Dict[str,typing.Union[str,typing.Callable]]
ListItems=typing.List[FunctionItem]
# !DEFINIENDO TIPO PARA PARÁMETRO
def init_interface(list_functions:ListItems):
    print('Bienvenido, escoge una función. (Ingresa 0 para salir): ')
    print('-------------------------------')
    for index,item in enumerate(list_functions):
        print(f"\n{int(index)+1}._ {item['name']}: {item['description']}")
    option=None
    while option!= 0:
        print('')
        input_option=input('Ingresa una opción: ')
        print('')
        if not input_option.isdigit():
            print('Debe ingresar un número.')
            continue
        option=int(input_option)
        if option==0:
            print('Saliendo...')
            break
        if not (option >= 1 and option <= len(list_functions)):
            print('Opción no válida')
            continue
        list_functions[option-1]['callback']()
    