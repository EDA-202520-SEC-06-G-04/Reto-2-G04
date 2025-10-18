import time
import csv
import sys
import os
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
               "taxis" : None
        } 
    catalog["neighborhood"] = data_structure.new_list()
    catalog["taxis"] = data_structure.new_list()
    return catalog

def load_taxis_data(catalog, file_t):
    """
    Carga los datos del reto
    """
    file_t = "Data/taxis-large.csv"
    input_del_archivo = csv.DictReader(open(file_t, encoding="utf-8"))
    for taxi in input_del_archivo:
        al.add_last(catalog['taxis'], taxi)
        size = al.size(catalog['taxis'])
    return size
    
def load_neighborhoods_data(catalog, file_n):
    """
    Carga los datos del reto
    """
    file_n = "Data/taxis-large.csv"
    input_del_archivo = csv.DictReader(open(file_n, encoding="utf-8"))
    for neighborhood in input_del_archivo:
        file_n = "Data/nyc-neighborhoods.csv"
        al.add_last(catalog['neighborhoods'], neighborhood)
        size = al.size(catalog['neighborhoods'])
    return size

def req_1(catalog, ):
    
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
    

def req_4(catalog):
    
    pass


def req_5(catalog, datehour, N):
    
    pass

def req_6(catalog, datehour, N):
    pass
