from entrenos import *

def prueba_lee_entrenos():
    ruta_fichero = 'data/entrenos.csv' # Ruta del archivo entrenos.csv dentro de la carpeta data
    entrenos = lee_entrenos(ruta_fichero)
    print('Los tres primeros entrenos:')
    for entreno in entrenos[:3]:
        print(entreno)
    print('\nLos tres últimos entrenos:')
    for entreno in entrenos[-3:]:
        print(entreno)
def prueba_tipos_entreno():
    ruta_fichero = 'data/entrenos(ruta_fichero)'
    entrenos = lee_entrenos(ruta_fichero)
    tipos = tipos_entreno(entrenos)
    print('Tipos de entreno en orden alfabético:')
    print(tipos)

def prueba_entrenos_duracion_superior():
    ruta_fichero = 'data/entrenos.csv'
    entrenos = lee_entrenos(ruta_fichero)
    duracion_superior = entrenos_duracion_superior(entrenos, 45)
    print(f'Entrenamientos con duracion superior a 45 minutos:')
    for entreno in duracion_superior:
        print(entreno)

def prueba_suma_calorias():
    ruta_fichero = 'data/entrenos.csv'
    entrenos = lee_entrenos(ruta_fichero)
    f_inicio = datetime.strptime('01/11/2021 00:00', '%d/%m/%Y %H:%M')
    f_fin = datetime.strptime('30/11/2021 23:59', '%d/%m/%Y %H:%M')

    total_calorias = suma_calorias(entrenos. f_inicio, f_fin)
    print(f'Suma de calorías quemadas entre el {f_inicio} y el {f_fin}: {total_calorias} kcal')

if __name__ == '__main__':
    prueba_lee_entrenos()
    prueba_tipos_entreno()
    prueba_entrenos_duracion_superior()
    prueba_suma_calorias()