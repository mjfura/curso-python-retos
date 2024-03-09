from control_de_flujo.sumatoria import sumatoria
from control_de_flujo.sumatoria_mejorada import sumatoria_mejorada
from control_de_flujo.sumatoria_series import sumatoria_series
from control_de_flujo.mostrar_multiplos import mostrar_multiplos
from funciones.velocidad_respuesta import carrera
from funciones.calcular_primo import calcular_primo
from views.interface import init_interface,ListItems

list_functions:ListItems=[{
    'name':'Sumatoria',
    'description':'Define un número de elementos y al final de ingresarlos realiza la suma de estos',
    'callback':sumatoria
},{
    'name':'Sumatoria Mejorada',
    'description':'Suma una lista de números que vas ingresando hasta  que ingresas 0. Y al final te muestra el total.',
    'callback':sumatoria_mejorada
},{
    'name':'Sumatoria Series',
    'description':'Función que calcula la sumatoria de pares de números hasta que la suma de un par sea 0.',
    'callback':sumatoria_series
},{
    'name':'Mostrar Múltiplos',
    'description':'Muestra los múltiplos de una lista de números 3 y 5 en este caso, dentro de un rango de números (0-100)',
    'callback':lambda :mostrar_multiplos([3,5],0,100)
},{
    'name':'Medidor de velocidad de respuesta',
    'description':'Medidor de velocidad de respuesta, debe presionar enter cuando salga el mensaje.',
    'callback':carrera
},{
    'name':'Calcular Primo',
    'description':'Muestra los primeros cien números primos',
    'callback':lambda :calcular_primo(100)
}]
init_interface(list_functions)