import sys
from tabulate import tabulate
from App import logic
from DataStructures.Lists import array_list as al
from DataStructures.Lists import single_linked_list as sl
from App import logic as lg

def new_logic():
    """
    Crea una instancia de la lógica según la estructura de datos seleccionada
    """
    print("Seleccione la estructura de datos que desea usar:")
    print("1 - Array List")
    print("2 - Single Linked List")
    estructura = input("Ingrese el número de la estructura (1 o 2): ")

    control = lg.new_logic(estructura)
    return control


def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename = "Data/taxis-test.csv"
    catalog = lg.load_data(control, filename)
    print("Taxis cargados:", al.size(catalog["array_list"]))


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    table=[]
    start=input("Ingrese la fecha de inicio en formato  (%Y-%m-%d %H:%M:%S):")
    end=input("Ingrese la fecha final en formato  (%Y-%m-%d %H:%M:%S):")
    quantity=int(input("Ingrese la cantidad de trayectos a mostrar:"))
    data=logic.req_1(control,start,end,quantity)
    counter,answer,total_time,first,last=data
    table.append(["Tiempo de carga en ms", total_time])
    table.append(["Total de trayectos que cumplieron con el filtro", counter])
    if answer==None:
        for taxi in range(logic.al.size(first)):
            t=logic.al.get_element(first, taxi)
            table.append(formato_tabla("primeros trayectos", t))
        for taxi in range(logic.al.size(last)):
            t=logic.al.get_element(last, taxi)
            table.append(formato_tabla("ultimos trayectos", t))
    else:
        for taxi in range(logic.al.size(answer)):
            t=logic.al.get_element(answer, taxi)
            table.append(formato_tabla("todos los trayectos trayectos", t))
    print(tabulate(table,headers=["Datos", "Valores"], tablefmt="grid"))

def formato_tabla(prefix, t):
    inicio=t["start"]
    lat_s= [round(t["pickup_lat"], 2), round(t["pickup_long"],2)]
    fin=t["end"]
    lat_e= [round(t["dropoff_lat"], 2), round(t["dropoff_long"],2)]
    distancia= t["trip_distance"]
    costo=t["total"]
    return [f"{prefix}: {inicio}, Fin: {fin}, latitud_longitud_i: {lat_s}, latitud_longitud_f: {lat_e}, Distancia: {distancia}, Costo: {costo}"]


def print_req_2(control):
    """|
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    lat_min = float(input("Ingrese la latitud mínima: "))
    lat_max = float(input("Ingrese la latitud máxima: "))
    N = int(input("Ingrese el número de trayectos a mostrar (N): "))

    result = logic.req_2(control, lat_min, lat_max, N)

    print("\n=== Resultado Requerimiento 2 ===")
    print(f"Tiempo de ejecución: {result['time_ms']} ms")
    print(f"Total de trayectos encontrados: {result['total']}")


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    min_distance=float(input("Ingrese la distancia minima (millas):"))
    max_distance=float(input("Ingrese la distancia maxima (millas):"))
    size_muestra=int(input("Ingrese el tamaño de la muestra:"))

    resultado= logic.req_3(control, min_distance, max_distance, size_muestra)
    print("Tiempo de ejecucion:", resultado[0], "ms")
    print("Numero de trayectos en el rango", resultado[1])
    headers=["Fecha-recogida", "Lat,long-recogida", "Fecha-terminacion", "Lat,Long-terminacion", "Distancia (mi)", "Costo(USD)"]
 
    if resultado[1] >=size_muestra*2:
        tabla_primeros= [[
            trayecto["pickup_datetime"],
            f"[{round(float(trayecto["pickup_latitude"]), 4)}, {round(float(trayecto["pickup_longitude"]),4)}]",
            trayecto["dropoff_datetime"],
            f"[{round(float(trayecto["dropoff_latitude"]), 4)}, {round(float(trayecto["dropoff_longitude"]),4)}]",
            round(float(trayecto["trip_distance"]), 2),
            round(float(trayecto["total_amount"]), 2)
            ] for trayecto in resultado[2]["elements"]]
        
        tabla_ultimos= [[
            trayecto["pickup_datetime"],
            f"[{round(float(trayecto["pickup_latitude"]), 4)}, {round(float(trayecto["pickup_longitude"]),4)}]",
            trayecto["dropoff_datetime"],
            f"[{round(float(trayecto["dropoff_latitude"]), 4)}, {round(float(trayecto["dropoff_longitude"]),4)}]",
            round(float(trayecto["trip_distance"]), 2),
            round(float(trayecto["total_amount"]), 2)
            ] for trayecto in resultado[3]["elements"]]
    
        print("\nPrimeros", size_muestra, "trayectos")
        print(tabulate(tabla_primeros, headers=headers, tablefmt="fancy_grid"))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    datehour = input("Ingrese la fecha y hora (formato YYYY-MM-DD HH): ")
    N = int(input("Ingrese el número de trayectos a mostrar (N): "))

    result = logic.req_5(control, lat_min, lat_max, N)

    print("\n=== Resultado Requerimiento 5 ===")
    print(f"Tiempo de ejecución: {result['time_ms']} ms")
    print(f"Total de trayectos encontrados: {result['total']}")


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
