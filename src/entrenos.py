import csv
from datetime import datetime
from collections import namedtuple

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido') # Sintaxix para crear una tupla con nombre

def parsea_compartido(dato):
    if dato=='S':
        return True
    elif dato=='N':
        return False

def lee_entrenos(ruta_fichero):
    '''
    Reibe la ruta del fichero en formato CSV codificado en utf-8 y 
    devuelve una lista de tuplas de tipo Entreno
    '''
    entrenos = [] 
    with open(ruta_fichero, newline= '', encoding='utf-8') as f:
        lector_csv = csv.reader(f)
        next(lector_csv)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector_csv:
            tipo=str(tipo)
            fechahora=datetime.strptime(fechahora, '%d/%m/%Y %H:%M'),
            ubicacion=str(ubicacion),
            duracion=int(duracion),
            calorias=int(calorias),
            distancia=float(distancia),
            frecuencia=int(frecuencia),
            compartido=parsea_compartido(compartido)
            
            entreno = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            entrenos.append(entrenos)

    return entrenos

def tipos_entrenos(entrenos):
    '''Devuelve una lista con todos los tipos de 
    entrenamientos en orden alfabético y sin repeticiones
    '''
    tipos = sorted({entreno.tipo for entreno in entrenos})
    return tipos

def entrenos_duracion_superior(entrenos, d):
    '''Fltramos los entrenos que tienen 
    una duración mayor a d
    '''
    listasupd=[]
    for entreno in entrenos:
        if entreno.duracion>d:
            listasupd
    return entreno
# Si no funciona: return[entreno for entrenoein entrenos if entreno.duracion >d]

def suma_calorias(entrenos, f_inicio, f_fin):
    '''Devuelve la suma de calorías quemadas en 
    entrenamientos realizados entre dos fechas
    ambas incluidas
    '''
    suma = 0 # Le doy un valor inicual a la suma y se van sumando los valores de cada calorias
    for e in entrenos:
        if f_inicio <= e.fechahora <= f_fin:
          suma += e.calorias
    return suma
          
             