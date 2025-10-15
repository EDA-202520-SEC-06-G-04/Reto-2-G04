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

def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


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


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

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
