import time
import csv
import sys
from math import asin, sin, cos, sqrt, radians
from datetime import datetime

from DataStructures.Lists import array_list as al
from DataStructures.Lists import single_linked_list as sl
from DataStructures.Queue import queue as q
from DataStructures.Stack import stack as st
from DataStructures.Maps import map_linear_probing as lp
from DataStructures.Maps import map_separate_chaining as sc 

data_structure = None

def new_logic(user_data_structure):
    if user_data_structure == "1":
        data_structure = al
    else:
        data_structure = sl

    catalog = {"neighborhood":None,
               "Taxis" : None
        } 
    catalog["neighborhood"] = data_structure.new_list()
    catalog["Taxis"] = data_structure.new_list()
    return catalog

def load_taxis_data(catalog, file_t):
    """
    Carga los datos del reto
    """
    file_t = 'data_dir' + 'taxis-large.csv'
    input_del_archivo = csv.DictReader(open(file_t, encoding="utf-8"))
    for taxi in input_del_archivo:
        al.add_last(catalog['taxis'], taxi)
        size = al.size(catalog['taxis'])
    return size
    
def load_neighborhoods_data(catalog, file_n):
    """
    Carga los datos del reto
    """
    file_n =  'data_dir' + 'nyc-neighbothoods.csv'
    input_del_archivo = csv.DictReader(open(file_n, encoding="utf-8"))
    for neighborhood in input_del_archivo:
        al.add_last(catalog['neighborhoods'], neighborhood)
    size = al.size(catalog['neighbothoods'])
    return size

def req_1(catalog, fecha_y_hora_inicial, fecha_y_hora_final, tamanio_muestra):
    
    start_time = get_time()
    
    pickup_time = datetime.datetime.strptime(fecha_y_hora_inicial,"%Y - %m - %d %H:%M:%S")
    dropoff_time = datetime.datetime.strptime(fecha_y_hora_final,"%Y - %m - %d %H:%M:%S")
        
    for viajes in catalog["taxis"]:
        elementos_filtrados = 0
        filtro = al.new_list()
        pickup_datetime_taxi = catalog["taxis"]["pickup_datetime"][viajes]
        dropoff_datetime_taxi = catalog["taxis"]["dropoff_datetime"][viajes]
        
        if pickup_datetime_taxi >= pickup_time and dropoff_datetime_taxi <= dropoff_time:
            al.add_last(filtro, catalog["taxis"])
            elementos_filtrados += 1
        sort_crit = al.default_sort_criteria(pickup_datetime_taxi,pickup_time)
        al.quick_sort(filtro, sort_crit)
            
        if elementos_filtrados <= (2 * tamanio_muestra):
            rta = filtro
                
        else:
            primero = al.sub_list(filtro,0,tamanio_muestra)
            size = al.size(filtro)
            ultimo = al.sub_list(filtro, size, tamanio_muestra) 
            rta = primero,ultimo   
        
    end_time = get_time()      
    tiempo = delta_time(start_time, end_time)            
  
    return elementos_filtrados,rta,tiempo


def req_2(catalog, lat_min, lat_max, N):
    """
    Retorna el resultado del requerimiento 2
    """
    import time
    start = time.process_time()

    trips = catalog['trips']
    filtered = [t for t in trips if lat_min <= float(t['pickup_latitude']) <= lat_max]

    filtered.sort(key=lambda t: (float(t['pickup_latitude']), float(t['pickup_longitude'])), reverse=True)

    total = len(filtered)
    end = time.process_time()
    time_ms = (end - start) * 1000

    if total <= 2 * N:
        first, last = filtered, []
    else:
        first, last = filtered[:N], filtered[-N:]

    return {
        'time_ms': round(time_ms, 2),
        'total': total,
        'first': first,
        'last': last
    }
    


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, fecha_terminacion, momento, tiempo_referencia, tamanio_muestra):
    
    start_time = get_time()
    elementos_filtrados = 0
    limite = False
    previo = sc.new_map(tamanio_muestra, 4)
    posterior = sc.new_map(tamanio_muestra, 4)
    filtro = al.new_list()
    
    fecha_ref = datetime.datetime.strptime(fecha_terminacion, "%Y-%m-%d").date()
    hora_ref = datetime.datetime.strptime(tiempo_referencia, "%H:%M:%S").time()

    for viajes in catalog["taxis"]:
        dropoff_datetime_taxi = catalog["taxis"]["dropoff_datetime"][viajes]

        if dropoff_datetime_taxi.date() == fecha_ref:
            if momento == "DESPUES" and dropoff_datetime_taxi.time() > hora_ref:
                al.add_last(filtro, catalog["taxis"][viajes])
                elementos_filtrados += 1
            elif momento == "ANTES" and dropoff_datetime_taxi.time() < hora_ref:
                al.add_last(filtro, catalog["taxis"][viajes])
                elementos_filtrados += 1
    
    al.selection_sort(filtro, "dropoff_datetime")

    if elementos_filtrados <= (2 * tamanio_muestra):
        rta = filtro
    else:
        primero = al.sub_list(filtro, 0, tamanio_muestra)
        size = al.size(filtro)
        ultimo = al.sub_list(filtro, size - tamanio_muestra, tamanio_muestra)

        rta = al.new_list()
        for i in range(al.size(primero)):
            al.add_last(rta, al.get_element(primero, i))
        for j in range(al.size(ultimo)):
            al.add_last(rta, al.get_element(ultimo, j))


    sc.put(previo, "cantidad_viajes", elementos_filtrados)
    sc.put(posterior, "muestra", rta)

    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    
    return elementos_filtrados, rta, tiempo


def req_5(catalog, datehour, N):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    import time
    from datetime import datetime

    start = time.process_time()

    hash_table = catalog['hash_dropoff']  
    trips = hash_table.get(datehour, [])  

    trips.sort(key=lambda t: datetime.strptime(t['dropoff_datetime'], "%Y-%m-%d %H:%M:%S"), reverse=True)

    total = len(trips)
    end = time.process_time()
    time_ms = (end - start) * 1000

    if total <= 2 * N:
        first, last = trips, []
    else:
        first, last = trips[:N], trips[-N:]

    return {
        'time_ms': round(time_ms, 2),
        'total': total,
        'first': first,
        'last': last
    }

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
