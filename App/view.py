import sys
import tabulate
import logic as lg
from DataStructures.Lists import array_list as al
from DataStructures.Lists import single_linked_list as sl
from DataStructures.Maps import map_separate_chaining as sc 


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
    Imprime los datos de un registro dado su ID.
    """
    datos = lg.get_data(control, id)
    
    if datos is None:
        print("No se encontró un registro con ese ID.")
        return
    
    print("Información del registro:")
    headers = ["Campo", "Valor"]
    rows = [[key, value] for key, value in datos.items()]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    fecha_y_hora_inicial = input("Digite la fecha y hora inicial (formato %Y-%m-%d %H:%M:%S): ").strip()
    fecha_y_hora_final = input("Digite la fecha y hora final (formato %Y-%m-%d %H:%M:%S): ").strip()
    tamanio_muestra = int(input("Digite el tamaño de la muestra N: ").strip())
    total, muestra, tiempo = lg.req_1(control, fecha_y_hora_inicial, fecha_y_hora_final, tamanio_muestra)
    if al.size(muestra) == 0:
        print("No se encontraron trayectos para los criterios dados.")
        return
    print("\nTiempo de la ejecución del requerimiento en milisegundos:", tiempo)
    print("Número total de trayectos que cumplieron el filtro de fecha y hora de recogida:", total)
    headers = [
        "Tiempo qie toma en ejecutarse la función",
        "Fecha y tiempo de recogida (AAAA-MM-DD HH:MM:SS) – criterio de ordenamiento",
        "Latitud y longitud de recogida ([Latitud, Longitud])",
        "Fecha y tiempo de terminación (AAAA-MM-DD HH:MM:SS)",
        "Latitud y longitud de terminación ([Latitud, Longitud])",
        "Distancia recorrida (millas)",
        "Costo total pagado"
    ]
    rows = []
    for viaje in muestra:
        rows.append([
            viaje['pickup_datetime'],
            f"[{viaje['pickup_latitude']}, {viaje['pickup_longitude']}]",
            viaje['dropoff_datetime'],
            f"[{viaje['dropoff_latitude']}, {viaje['dropoff_longitude']}]",
            viaje['trip_distance'],
            viaje['total_amount']
        ])
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def print_req_2(control):
    """|
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    lat_min = float(input("Ingrese la latitud mínima: "))
    lat_max = float(input("Ingrese la latitud máxima: "))
    N = int(input("Ingrese el número de trayectos a mostrar (N): "))

    result = control.req_2(control, lat_min, lat_max, N)

    print("\n=== Resultado Requerimiento 2 ===")
    print(f"Tiempo de ejecución: {result['time_ms']} ms")
    print(f"Total de trayectos encontrados: {result['total']}")

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    fecha_terminacion = input("Digite la fecha de terminación (formato %Y-%m-%d): ").strip()
    momento = input("Digite el momento de interés ('ANTES' o 'DESPUES'): ").strip().upper()
    tiempo_referencia = input("Digite el tiempo de referencia (formato %H:%M:%S): ").strip()
    tamanio_muestra = int(input("Digite el tamaño de la muestra N: ").strip())
    
    total, muestra, tiempo = lg.req_4(control, fecha_terminacion, momento, tiempo_referencia, tamanio_muestra)
    
    if total == 0:
        print("No se encontraron trayectos para los criterios dados.")
        return
    
    print("\nTiempo de la ejecución del requerimiento en milisegundos:", tiempo)
    print("Número total de trayectos que cumplieron el filtro de fecha y hora de terminación:", total)
    
    headers = [
        "Fecha y tiempo de recogida (AAAA-MM-DD HH:MM:SS)",
        "Latitud y longitud de recogida ([Latitud, Longitud])",
        "Fecha y tiempo de terminación (AAAA-MM-DD HH:MM:SS) – criterio de ordenamiento",
        "Latitud y longitud de terminación ([Latitud, Longitud])",
        "Distancia recorrida (millas)",
        "Costo total pagado"
    ]
    
    rows = []
    
    if type(muestra) == tuple:
        primero, ultimo = muestra
        for viaje in primero:
            rows.append([
                viaje['pickup_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                f"[{viaje['pickup_latitude']:.6f}, {viaje['pickup_longitude']:.6f}]",
                viaje['dropoff_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                f"[{viaje['dropoff_latitude']:.6f}, {viaje['dropoff_longitude']:.6f}]",
                f"{viaje['trip_distance']:.2f}",
                f"{viaje['total_amount']:.2f}"
            ])
        if al.size(ultimo) > 0:
            rows.append(["--- Últimos N ---", "", "", "", "", ""])
        for viaje in ultimo:
            rows.append([
                viaje['pickup_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                f"[{viaje['pickup_latitude']:.6f}, {viaje['pickup_longitude']:.6f}]",
                viaje['dropoff_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                f"[{viaje['dropoff_latitude']:.6f}, {viaje['dropoff_longitude']:.6f}]",
                f"{viaje['trip_distance']:.2f}",
                f"{viaje['total_amount']:.2f}"
            ])
    else:
        for viaje in muestra:
            rows.append([
                viaje['pickup_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                f"[{viaje['pickup_latitude']:.6f}, {viaje['pickup_longitude']:.6f}]",
                viaje['dropoff_datetime'].strftime('%Y-%m-%d %H:%M:%S'),
                f"[{viaje['dropoff_latitude']:.6f}, {viaje['dropoff_longitude']:.6f}]",
                f"{viaje['trip_distance']:.2f}",
                f"{viaje['total_amount']:.2f}"
            ])
    
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola
    """
    hora_terminacion = input("Digite la fecha y hora de terminación (formato %Y-%m-%d %H): ").strip()
    tamanio_a_mostrar = int(input("Digite el tamaño de la muestra N: ").strip())
    total, muestra, tiempo = lg.req_5(control, hora_terminacion, tamanio_a_mostrar)
    if al.size(muestra) == 0:
        print("No se encontraron trayectos para los criterios dados.")
        return
    print("\nTiempo de la ejecución del requerimiento en milisegundos:", tiempo)
    print("Número total de trayectos que cumplieron el filtro de fecha y hora de terminación:", total)
    headers = [
        "Fecha y tiempo de recogida (AAAA-MM-DD HH:MM:SS)",
        "Latitud y longitud de recogida ([Latitud, Longitud])",
        "Fecha y tiempo de terminación (AAAA-MM-DD HH:MM:SS)",
        "Latitud y longitud de terminación ([Latitud, Longitud])",
        "Distancia recorrida (millas)",
        "Costo total pagado"
    ]
    rows = []
    if total <= 2 * tamanio_a_mostrar:
        for viaje in muestra:
            rows.append([
                viaje['pickup_datetime'],
                f"[{float(viaje['pickup_latitude']):.6f}, {float(viaje['pickup_longitude']):.6f}]",
                viaje['dropoff_datetime'],
                f"[{float(viaje['dropoff_latitude']):.6f}, {float(viaje['dropoff_longitude']):.6f}]",
                f"{float(viaje['trip_distance']):.2f}",
                f"{float(viaje['total_amount']):.2f}"
            ])
    else:
        primero = al.sub_list(muestra, 0, tamanio_a_mostrar)
        ultimo = al.sub_list(muestra, al.size(muestra) - tamanio_a_mostrar, tamanio_a_mostrar)
        for viaje in primero:
            rows.append([
                viaje['pickup_datetime'],
                f"[{float(viaje['pickup_latitude']):.6f}, {float(viaje['pickup_longitude']):.6f}]",
                viaje['dropoff_datetime'],
                f"[{float(viaje['dropoff_latitude']):.6f}, {float(viaje['dropoff_longitude']):.6f}]",
                f"{float(viaje['trip_distance']):.2f}",
                f"{float(viaje['total_amount']):.2f}"
            ])
        if al.size(ultimo) > 0:
            rows.append(["--- Últimos N ---", "", "", "", "", ""])
        for viaje in ultimo:
            rows.append([
                viaje['pickup_datetime'],
                f"[{float(viaje['pickup_latitude']):.6f}, {float(viaje['pickup_longitude']):.6f}]",
                viaje['dropoff_datetime'],
                f"[{float(viaje['dropoff_latitude']):.6f}, {float(viaje['dropoff_longitude']):.6f}]",
                f"{float(viaje['trip_distance']):.2f}",
                f"{float(viaje['total_amount']):.2f}"
            ])
    print("\nMostrar la siguiente información de cada uno de los N primeros trayectos y de los N últimos trayectos:")
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def print_req_6(control):
    """
    Función que imprime la solución del Requerimiento 6 en consola
    """    
    neighborhood_name = input("Digite el nombre del barrio: ").strip()
    hora_inicial = input("Digite la hora inicial (formato HH): ").strip()
    hora_final = input("Digite la hora final (formato HH): ").strip()
    N = int(input("Digite el tamaño de la muestra N: ").strip())
    total, muestra, tiempo = lg.req_6(control, neighborhood_name, hora_inicial, hora_final, N)
    if al.size(muestra) == 0:
        print("No se encontraron trayectos para los criterios dados.")
        return
    print("\nTiempo de la ejecución del requerimiento en milisegundos:", tiempo)
    print("Número total de trayectos que cumplieron el filtro:", total)
    headers = [
        "Fecha y tiempo de recogida (AAAA-MM-DD HH:MM:SS)",
        "Latitud y longitud de recogida ([Latitud, Longitud])",
        "Fecha y tiempo de terminación (AAAA-MM-DD HH:MM:SS)",
        "Latitud y longitud de terminación ([Latitud, Longitud])",
        "Distancia recorrida (millas)",
        "Costo total pagado"
    ]
    rows = []
    if total <= 2 * N:
        for viaje in muestra:
            rows.append([
                viaje['pickup_datetime'],
                f"[{viaje['pickup_coords'][0]:.6f}, {viaje['pickup_coords'][1]:.6f}]",
                viaje['dropoff_datetime'],
                f"[{viaje['dropoff_coords'][0]:.6f}, {viaje['dropoff_coords'][1]:.6f}]",
                f"{viaje['trip_distance']:.2f}",
                f"{viaje['total_amount']:.2f}"
            ])
    else:
        primero = al.sub_list(muestra, 0, N)
        ultimo = al.sub_list(muestra, al.size(muestra) - N, N)
        for viaje in primero:
            rows.append([
                viaje['pickup_datetime'],
                f"[{viaje['pickup_coords'][0]:.6f}, {viaje['pickup_coords'][1]:.6f}]",
                viaje['dropoff_datetime'],
                f"[{viaje['dropoff_coords'][0]:.6f}, {viaje['dropoff_coords'][1]:.6f}]",
                f"{viaje['trip_distance']:.2f}",
                f"{viaje['total_amount']:.2f}"
            ])
        if al.size(ultimo) > 0:
            rows.append(["--- Últimos N ---", "", "", "", "", ""])
        for viaje in ultimo:
            rows.append([
                viaje['pickup_datetime'],
                f"[{viaje['pickup_coords'][0]:.6f}, {viaje['pickup_coords'][1]:.6f}]",
                viaje['dropoff_datetime'],
                f"[{viaje['dropoff_coords'][0]:.6f}, {viaje['dropoff_coords'][1]:.6f}]",
                f"{viaje['trip_distance']:.2f}",
                f"{viaje['total_amount']:.2f}"
            ])
    print("\nMostrar la siguiente información de cada uno de los N primeros trayectos y de los N últimos trayectos:")
    print(tabulate(rows, headers=headers, tablefmt="grid"))


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

        #elif int(inputs) == 3:
            #print_req_3(control)

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
