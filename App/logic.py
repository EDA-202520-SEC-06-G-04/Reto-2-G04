import time
from time import perf_counter
from typing import List, Dict, Any
from datetime import datetime
import math
from DataStructures.List import single_linked_list as lt
Record = Dict[str, Any]
def new_logic(user_data_structure):
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    pass



# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


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


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


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
