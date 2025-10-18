import time
import csv
import sys
import math
import os
from math import asin, sin, cos, sqrt, radians
import datetime 

from DataStructures.Lists import array_list as al
from DataStructures.Lists import single_linked_list as sl
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
    size = al.size(catalog['neighbothoods'])
    return size  


def sort_crit_time(v1, v2):
    dt1 = datetime.datetime.strptime(v1["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.datetime.strptime(v2["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
    return al.default_sort_criteria(dt1, dt2)
       
def req_1(catalog, fecha_y_hora_inicial, fecha_y_hora_final, tamanio_muestra):   
    start_time = get_time()
  
    pickup_time = datetime.datetime.strptime(fecha_y_hora_inicial, "%Y-%m-%d %H:%M:%S")
    dropoff_time = datetime.datetime.strptime(fecha_y_hora_final, "%Y-%m-%d %H:%M:%S")
    
    elementos_filtrados = 0
    quedan = al.new_list()
    
    for viaje in catalog["taxis"]:
        pickup_datetime_taxi = datetime.datetime.strptime(viaje["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        dropoff_datetime_taxi = datetime.datetime.strptime(viaje["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
       
        if pickup_datetime_taxi >= pickup_time and dropoff_datetime_taxi <= dropoff_time:
            al.add_last(quedan, viaje)
            elementos_filtrados += 1    
    
    quedan = al.merge_sort(quedan, sort_crit_time)
        
    if elementos_filtrados <= (2 * tamanio_muestra):
        rta = quedan
    else:
        primero = al.sub_list(quedan, 0, tamanio_muestra)
        size = al.size(quedan)
        ultimo = al.sub_list(quedan, size - tamanio_muestra, tamanio_muestra)
        rta = al.new_list()
        for i in range(al.size(primero)):
            al.add_last(rta, al.get_element(primero, i))
        for i in range(al.size(ultimo)):
            al.add_last(rta, al.get_element(ultimo, i))
    
    end_time = get_time()      
    tiempo = delta_time(start_time, end_time)            
  
    return elementos_filtrados, rta, tiempo

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass

def req_4(catalog, fecha_terminacion, momento, tiempo_referencia, tamanio_muestra):
   
    start_time = get_time()
    fecha_term = datetime.datetime.strptime(fecha_terminacion, "%Y-%m-%d").date()
    tiempo_ref = datetime.datetime.strptime(tiempo_referencia, "%H:%M:%S").time()
    
    my_table = sc.new_map(1000, 4)
    
    for viaje in catalog["taxis"]:
        dropoff_datetime_str = viaje["dropoff_datetime"]
        dropoff_datetime = datetime.datetime.strptime(dropoff_datetime_str, "%Y-%m-%d %H:%M:%S")
        fecha_drop = dropoff_datetime.date()
        
        if not sc.contains(my_table, fecha_drop):
            sc.put(my_table, fecha_drop, al.new_list())
        lista_fecha = sc.get(my_table, fecha_drop)
        al.add_last(lista_fecha, viaje)
    
    if sc.contains(my_table, fecha_term):
        lista_filtrada = al.new_list()
        lista_fecha = sc.get(my_table, fecha_term)
        
        for viaje in lista_fecha:
            dropoff_time = datetime.datetime.strptime(viaje["dropoff_datetime"], "%Y-%m-%d %H:%M:%S").time()
            if momento == "ANTES" and dropoff_time < tiempo_ref:
                al.add_last(lista_filtrada, viaje)
            elif momento == "DESPUES" and dropoff_time > tiempo_ref:
                al.add_last(lista_filtrada, viaje)
        
        elementos_filtrados = al.size(lista_filtrada)        
        lista_filtrada = al.merge_sort(lista_filtrada, sort_crit_time)
        
        if elementos_filtrados <= (2 * tamanio_muestra):
            muestra = lista_filtrada
        else:
            primero = al.sub_list(lista_filtrada, 0, tamanio_muestra)
            size = al.size(lista_filtrada)
            ultimo = al.sub_list(lista_filtrada, size - tamanio_muestra, tamanio_muestra)
            muestra = al.new_list()
            for pos in primero:
                al.add_last(muestra, pos)
            for pos in ultimo:
                al.add_last(muestra, pos)
    else:
        elementos_filtrados = 0
        muestra = al.new_list()
    
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    
    return elementos_filtrados, muestra, tiempo

def sort_crit(v1, v2):
    dt1 = datetime.datetime.strptime(v1["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.datetime.strptime(v2["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
    return al.default_sort_criteria(dt2, dt1)

def req_5(catalog, hora_terminacion, tamanio_a_mostrar):
    start_time = get_time()
    
    hash_table = sc.new_map(10000, 4)
    for viaje in catalog["taxis"]:
        dropoff_datetime = datetime.datetime.strptime(viaje["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
        llave = dropoff_datetime.strftime("%Y-%m-%d %H")
        if not sc.contains(hash_table, llave):
            sc.put(hash_table, llave, al.new_list())
        lista_llave = sc.get(hash_table, llave)
        al.add_last(lista_llave, viaje)
    
    if sc.contains(hash_table, hora_terminacion):
        trips = sc.get(hash_table, hora_terminacion)
        
        trips = al.merge_sort(trips, sort_crit)
        
        total = al.size(trips)
        
        if total <= 2 * tamanio_a_mostrar:
            muestra = trips
        else:
            primero = al.sub_list(trips, 0, tamanio_a_mostrar)
            ultimo = al.sub_list(trips, total - tamanio_a_mostrar, tamanio_a_mostrar)
            muestra = al.new_list()
            for pos in primero:
                al.add_last(muestra, pos)
            for pos in ultimo:
                al.add_last(muestra, pos)
    else:
        total = 0
        muestra = al.new_list()

    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    
    return total, muestra, tiempo

def req_6(catalog, neighborhood_name, hora_inicial, hora_final, tamanio_a_mostrar):
    start_time = get_time()
    
    barrios = catalog["hash_neighborhoods"]
    if not sc.contains(barrios, neighborhood_name):
        return 0, al.new_list(), 0
    
    barrio_coords = sc.get(barrios, neighborhood_name)
    lat_barrio, lon_barrio = float(barrio_coords[0]), float(barrio_coords[1])
    
    trips = catalog["taxis"]
    filtrados = al.new_list()
    
    hora_i = int(hora_inicial)
    hora_f = int(hora_final)
    
    for viaje in trips:
        pickup_dt = datetime.datetime.strptime(viaje["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        hora_pickup = pickup_dt.hour
        pickup_lat = float(viaje["pickup_latitude"])
        pickup_lon = float(viaje["pickup_longitude"])
        
        R = 3958.8
        dlat = math.radians(pickup_lat - lat_barrio)
        dlon = math.radians(pickup_lon - lon_barrio)
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat_barrio)) * math.cos(math.radians(pickup_lat)) * math.sin(dlon / 2)**2
        distancia = 2 * R * math.asin(math.sqrt(a))
        
        if hora_i <= hora_pickup <= hora_f and distancia <= 0.2:
            viaje_filtrado = {
                "pickup_datetime": viaje["pickup_datetime"],
                "pickup_coords": (pickup_lat, pickup_lon),
                "dropoff_datetime": viaje["dropoff_datetime"],
                "dropoff_coords": (float(viaje["dropoff_latitude"]), float(viaje["dropoff_longitude"])),
                "trip_distance": float(viaje["trip_distance"]),
                "total_amount": float(viaje["total_amount"]),
                "distancia_barrio": distancia
            }
            al.add_last(filtrados, viaje_filtrado)
    
    def sort_crit(v1, v2):
        dt1 = datetime.datetime.strptime(v1["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        dt2 = datetime.datetime.strptime(v2["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
        return al.default_sort_criteria(dt1, dt2)
    
    filtrados = al.merge_sort(filtrados, sort_crit)
    
    total = al.size(filtrados)
    
    if total <= 2 * tamanio_a_mostrar:
        muestra = filtrados
    else:
        primero = al.sub_list(filtrados, 0, tamanio_a_mostrar)
        ultimo = al.sub_list(filtrados, total - tamanio_a_mostrar, tamanio_a_mostrar)
        muestra = al.new_list()
        for pos in primero:
            al.add_last(muestra, pos)
        for pos in ultimo:
            al.add_last(muestra, pos)
    
    end_time = get_time()
    tiempo = delta_time(start_time, end_time)
    
    return total, muestra, tiempo

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
