import os
import re
import json


# METODOS

def limpiarConsola():
    print("\nPresione para continuar...")
    input("")


def ImportarJson(nombre_archivo) -> list:
    '''
    Recibe un Json para importar a un lista

    Param:
    *nombre_archivo: nombre del archivo Json.

    Return:
    retorna un lista con la data
    '''
    with open(nombre_archivo, "r") as archivo:
        lista = json.load(archivo)

    return lista


def SeleccionarJugador(data) -> list:
    lista = []
    indice = 0

    for item in data["jugadores"]:
        dict = {}
        if "nombre" in item:
            nombre = item["nombre"]

            if nombre != "" and nombre not in dict:
                jugador = "{} - {}".format(nombre, indice)
                dict["nombre"] = nombre
                dict["indice"] = indice
                lista.append(dict)
                indice += 1

    return lista


def BuscarJugador(nombre: str) -> dict:
    '''
    Busca un jugador en especifico, ingrsando el nombre

    Param:
    *nombre: nombre del jugador a buscar

    Return:
    retorna un diccionario del jugador
    '''
    dict = []
    patron = re.compile(nombre, re.IGNORECASE)

    for item in listaJugadores["jugadores"]:
        if re.search(patron, item["nombre"]):
            dict.append(item)
            break

    return dict

# 1


def MostrarJugadores(data: list) -> list:
    '''
    Muestra los jugadores  con el formato [Nombre Jugador - Posición]

    Param:
    *data: lista con todos los jugadores

    Return:
    retorna una lista con la data
    '''

    lista = []

    for item in data["jugadores"]:
        if "nombre" in item:
            nombre = item["nombre"]
            posicion = item['posicion']

            if nombre != "" and posicion != "" and nombre not in lista:
                jugador = "{} - {}".format(nombre, posicion)
                lista.append(jugador)

    return lista

# 2


def MostrarJugadorEspecifico(data: list, opcion: int) -> dict:
    '''
    Muestra info del jugador elegido como temporadas jugadas, puntos totales,
    promedio de puntos por partido, rebotes totales, promedio de rebotes por partido,
    asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales,
    porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

    Param:
    *data: lista con todos los jugadores
    *opcion: num de la opcion elegida

    Return:
    retorna un diccionario con la data
    '''

    dicct = {}
    nombreJugador = ""

    for i in listaJugadores:
        print(i)

    opcion = input("\nIngrese INDICE del jugador seleccionado: ")

    for item in listaJugadores:
        if item["indice"] == int(opcion):
            nombreJugador = item["nombre"]
            break

    for item in data["jugadores"]:
        if item["nombre"] == nombreJugador:
            dicct = item["estadisticas"]
            dicct["nombre"] = nombreJugador
            return dicct


# 3
def GuardarEstadiscticasCSV(data: dict) -> bool:
    '''
    Guarda la info en un archivo csv

    Param:
    *data: diccionario con la informacion a guardar

    Return:
    retorna -true si lo guardo correctamente
            -false no guardo correctamente
    '''

    rutaArchivo = "C:/Users/olici/Desktop/U T N/1° AÑO/1° CUATRIMESTRE/Prog I - Python/{0}_estadisticas.csv"
    with open(rutaArchivo, "w") as archivo:
        for fila in data:
            linea = ",".join(str(valor) for valor in fila)
            archivo.write(linea + "\n")

    return True


# 4
def BuscarJugador(nombre: str) -> dict:
    '''
    Guarda la info en un archivo csv
    Param:
    *data: diccionario con la informacion a guardar
    Return:
    retorna -true si lo guardo correctamente
          -false no guardo correctamente
    '''
    dict = []
    patron = re.compile(nombre, re.IGNORECASE)
    for item in listaJugadores["jugadores"]:
        if re.search(patron, item["nombre"]):
            dict.append(item["nombre"])
            dict.append(item["logros"][0])
            dict.append(item["logros"][2])
            dict.append(item["logros"][6])
            break
    return dict
# 5


def CalcularMostrarPromedioPuntosXPartidoDeTodoEquipo(data: list):
    '''
    Muestra el promedio de puntos x partido de todo el equipo

    Param:
    *data: lista con la informacion del equipo
    '''

    n = len(data["jugadores"])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data["jugadores"][j]["estadisticas"]["promedio_puntos_por_partido"] < data["jugadores"][j + 1]["estadisticas"]["promedio_puntos_por_partido"]:
                data["jugadores"][j]["estadisticas"]["promedio_puntos_por_partido"], data["jugadores"][j + 1]["estadisticas"]["promedio_puntos_por_partido"] = data["jugadores"][j +
                                                                                                                                                                                 1]["estadisticas"]["promedio_puntos_por_partido"], data["jugadores"][j]["estadisticas"]["promedio_puntos_por_partido"]

    for jugador in data["jugadores"]:
        print(jugador["nombre"], jugador["estadisticas"]
              ["promedio_puntos_por_partido"])


# 6
def MostrarJugadorPerteneceAlSalonDeLaFama(data: list) -> bool:
    '''
    Determina si el jugador elegido pertenece al salon de la fama

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna -true si pertenece
            -false si no pertenece
    '''

    print(SeleccionarJugador(listaJugadores))
    nombre = input("Nombre: ")
    jugador = BuscarJugador(nombre)

    for item in jugador:
        if 'Miembro del Salon de la Fama del Baloncesto' in item["logros"]:
            return True

    return False


# 7
def MostrarJugadorConMayorCantidadRebotesTotales(data: list) -> dict:
    '''
    muestra el jugador con mayor cantidad de rebotes totales

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna un diccionario con la informacion del jugador
    '''

    dict = {}
    max = 0
    indice = 0

    for item in range(len(data["jugadores"])):
        if data["jugadores"][item]["estadisticas"]["rebotes_totales"] > max:
            max = data["jugadores"][item]["estadisticas"]["rebotes_totales"]
            indice = item

    dict["nombre"] = data["jugadores"][indice]["nombre"]
    dict["rebotes_totales"] = data["jugadores"][indice]["estadisticas"]["rebotes_totales"]

    return dict


# 8
def MostrarJugadorConMayorPorcentajeDeTirosDeCampo(data: list) -> dict:
    '''
    muestra el jugador con mayor porcentaje de tiros de campo totales

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna un diccionario con la informacion del jugador
    '''

    dict = {}
    max = 0
    indice = 0

    for item in range(len(data["jugadores"])):
        if float(data["jugadores"][item]["estadisticas"]["porcentaje_tiros_de_campo"]) > float(max):
            max = data["jugadores"][item]["estadisticas"]["porcentaje_tiros_de_campo"]
            indice = item

    dict["nombre"] = data["jugadores"][indice]["nombre"]
    dict["porcentaje_tiros_de_campo"] = float(
        data["jugadores"][indice]["estadisticas"]["porcentaje_tiros_de_campo"])

    return dict


# 9
def MostrarJugadorConMayorCantidadAsistenciasTotales(data: list) -> dict:
    '''
    muestra el jugador con mayor cantidad de asitencias totales

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna un diccionario con la informacion del jugador
    '''

    dict = {}
    max = 0
    indice = 0

    for item in range(len(data["jugadores"])):
        if float(data["jugadores"][item]["estadisticas"]["asistencias_totales"]) > float(max):
            max = data["jugadores"][item]["estadisticas"]["asistencias_totales"]
            indice = item

    dict["nombre"] = data["jugadores"][indice]["nombre"]
    dict["asistencias_totales"] = float(
        data["jugadores"][indice]["estadisticas"]["asistencias_totales"])

    return dict


# 10
def MostrarJugadoresConMayorPuntosIngresado(data: list):
    '''
    muestra el jugador con mayor puntos

    Param:
    *data: lista con la informacion del equipo

    '''
    lista = []
    valor = input("Ingrese Puntos: ")
    puntos = int(valor)

    for item in data["jugadores"]:
        if float(item["estadisticas"]["promedio_puntos_por_partido"]) > float(puntos):
            jugador = "{0} - {1}".format(item["nombre"], float(
                item["estadisticas"]["promedio_puntos_por_partido"]))
            if jugador != "":
                lista.append(jugador)

    if len(lista) < 1:
        print("No hay jugadores con esa cantidad ingresada")
    else:
        for item in lista:
            print(item)


# 11
def MostrarJugadoresConMayorRebotesIngresado(data: list):
    '''
    muestra el jugador con mayor cantidad de rebotes totales

    Param:
    *data: lista con la informacion del equipo

    '''

    lista = []
    valor = input("Ingrese Puntos: ")
    puntos = int(valor)

    for item in data["jugadores"]:
        if float(item["estadisticas"]["promedio_rebotes_por_partido"]) > float(puntos):
            jugador = "{0} - {1}".format(item["nombre"], float(
                item["estadisticas"]["promedio_rebotes_por_partido"]))
            if jugador != "":
                lista.append(jugador)

    if len(lista) < 1:
        print("No hay jugadores con esa cantidad ingresada")
    else:
        for item in lista:
            print(item)


# 12
def MostrarJugadoresConMayorAsistenciasIngresado(data: list):
    '''
    muestra el jugador con mayor asistencias

    Param:
    *data: lista con la informacion del equipo

    '''

    lista = []
    valor = input("Ingrese Puntos: ")
    puntos = int(valor)

    for item in data["jugadores"]:
        if float(item["estadisticas"]["promedio_asistencias_por_partido"]) > float(puntos):
            jugador = "{0} - {1}".format(item["nombre"], float(
                item["estadisticas"]["promedio_asistencias_por_partido"]))
            if jugador != "":
                lista.append(jugador)

    if len(lista) < 1:
        print("No hay jugadores con esa cantidad ingresada")
    else:
        for item in lista:
            print(item)


# 13
def MostrarJugadorConMayorCantidadRobosTotales(data: list) -> dict:
    '''
    muestra el jugador con mayor cantidad de robos totales

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna un diccionario con la informacion del jugador
    '''

    dict = {}
    max = 0
    indice = 0

    for item in range(len(data["jugadores"])):
        if float(data["jugadores"][item]["estadisticas"]["robos_totales"]) > float(max):
            max = data["jugadores"][item]["estadisticas"]["robos_totales"]
            indice = item

    dict["nombre"] = data["jugadores"][indice]["nombre"]
    dict["robos_totales"] = float(
        data["jugadores"][indice]["estadisticas"]["robos_totales"])

    return dict


# 14
def MostrarJugadorConMayorCantidadBloqueosTotales(data: list) -> dict:
    '''
    muestra el jugador con mayor cantidad de bloqueos totales

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna un diccionario con la informacion del jugador
    '''

    dict = {}
    max = 0
    indice = 0

    for item in range(len(data["jugadores"])):
        if float(data["jugadores"][item]["estadisticas"]["bloqueos_totales"]) > float(max):
            max = data["jugadores"][item]["estadisticas"]["bloqueos_totales"]
            indice = item

    dict["nombre"] = data["jugadores"][indice]["nombre"]
    dict["bloqueos_totales"] = float(
        data["jugadores"][indice]["estadisticas"]["bloqueos_totales"])

    return dict


# 15
def MostrarJugadoresConMayorPorcentajeDeTirosLibresIngresado(data: list):
    '''
    muestra el jugador con mayor porcentaje de tiros libres

    Param:
    *data: lista con la informacion del equipo

    '''

    lista = []
    valor = input("Ingrese Puntos: ")
    puntos = int(valor)

    for item in data["jugadores"]:
        if float(item["estadisticas"]["porcentaje_tiros_libres"]) > float(puntos):
            jugador = "{0} - {1}".format(item["nombre"], float(
                item["estadisticas"]["porcentaje_tiros_libres"]))
            if jugador != "":
                lista.append(jugador)

    if len(lista) < 1:
        print("No hay jugadores con esa cantidad ingresada")
    else:
        for item in lista:
            print(item)


# 16
def MostrarJugadoresConMayorPorcentajeDeTirosXPartidoExcluyendoAlUltimo(data: list):
    '''
    muestra el jugador con mayor porcentaje de tiros x partido [EXCLUYENDO AL ULTIMO]

    Param:
    *data: lista con la informacion del equipo

    '''

    lista = []
    n = len(data["jugadores"])
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data["jugadores"][j]["estadisticas"]["promedio_puntos_por_partido"] < data["jugadores"][j + 1]["estadisticas"]["promedio_puntos_por_partido"]:
                data["jugadores"][j]["estadisticas"]["promedio_puntos_por_partido"], data["jugadores"][j + 1]["estadisticas"]["promedio_puntos_por_partido"] = data["jugadores"][j +
                                                                                                                                                                                 1]["estadisticas"]["promedio_puntos_por_partido"], data["jugadores"][j]["estadisticas"]["promedio_puntos_por_partido"]

    for item in range(len(data["jugadores"])):
        jugador = "{0} {1}".format(data["jugadores"][item]["nombre"], data["jugadores"][item]["estadisticas"]
                                   ["promedio_puntos_por_partido"])
        lista.append(jugador)

    return lista[:-1]  # .pop()


# 17
def MostrarJugadorConMayorCantidadLogros(data: list) -> list:
    '''
    muestra el jugador con mayor cantidad de logros

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna una lista de el/los jugadores con mayor logros
    '''
    lista = []
    max = 0

    for item in range(len(data["jugadores"])):
        if int(len(data["jugadores"][item]["logros"])) >= max:
            max = int(len(data["jugadores"][item]["logros"]))

            dict = {}
            dict["nombre"] = data["jugadores"][item]["nombre"]
            dict["logros"] = len(data["jugadores"][item]["logros"])

            lista.append(dict)

    return lista


# 18
def MostrarJugadoresConMayorPorcentajeDeTirosTriplesIngresado(data: list):
    '''
    muestra el jugador con mayor porcentaje de tiros triples

    Param:
    *data: lista con la informacion del equipo

    '''

    lista = []
    valor = input("Ingrese Puntos: ")
    puntos = int(valor)

    for item in data["jugadores"]:
        if float(item["estadisticas"]["porcentaje_tiros_triples"]) > float(puntos):
            jugador = "{0} - {1}".format(item["nombre"], float(
                item["estadisticas"]["porcentaje_tiros_triples"]))
            if jugador != "":
                lista.append(jugador)

    if len(lista) < 1:
        print("No hay jugadores con esa cantidad ingresada")
    else:
        for item in lista:
            print(item)


# 19
def MostrarJugadorConMayorCantidadTempJugadas(data: list) -> dict:
    '''
    muestra el jugador con mayor cantidad de temp jugadas

    Param:
    *data: lista con la informacion del equipo

    Return:
    retorna un diccionario con la informacion del jugador
    '''

    dict = {}
    max = 0
    indice = 0

    for item in range(len(data["jugadores"])):
        if float(data["jugadores"][item]["estadisticas"]["temporadas"]) > float(max):
            max = data["jugadores"][item]["estadisticas"]["temporadas"]
            indice = item

    dict["nombre"] = data["jugadores"][indice]["nombre"]
    dict["temporadas"] = float(
        data["jugadores"][indice]["estadisticas"]["temporadas"])

    return dict


# 20
def MostrarJugadorConMayorPorcentajeTiroDeCampo(data: list):
    '''
    muestra el jugador con mayor porcentaje de tiro de campo

    Param:
    *data: lista con la informacion del equipo

    '''

    lista = []
    valor = input("Ingrese Puntos: ")
    puntos = int(valor)

    for jugador in data["jugadores"]:
        if float(jugador["estadisticas"]["porcentaje_tiros_de_campo"]) > puntos:
            lista.append(jugador)

    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j]["posicion"] > lista[j + 1]["posicion"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    for jugador in lista:
        print("{0} / {1} - Puntos: {2}".format(jugador["nombre"], jugador["posicion"],
                                               jugador["estadisticas"]["porcentaje_tiros_de_campo"]))


# CARGAR LISTA JUGADORES
listaJugadores = ImportarJson(
    "C:/Users/olici/Desktop/U T N/1° AÑO/1° CUATRIMESTRE/Prog I - Python/dt.json")


### MENU ###
while True:

    print("1. MostrarJugadores")
    print("2. MostrarJugadorEspecifico")
    print("3. GuardarEstadiscticasCSV")
    print("4. BuscarJugador")
    print("5. CalcularMostrarPromedioPuntosXPartidoDeTodoEquipo")
    print("6. MostrarJugadorPerteneceAlSalonDeLaFama")
    print("7. MostrarJugadorConMayorCantidadRebotesTotales")
    print("8. MostrarJugadorConMayorPorcentajeDeTirosDeCampo")
    print("9. MostrarJugadorConMayorCantidadAsistenciasTotales")
    print("10. MostrarJugadoresConMayorPuntosIngresado")
    print("11. MostrarJugadoresConMayorRebotesIngresado")
    print("12. MostrarJugadoresConMayorAsistenciasIngresado")
    print("13. MostrarJugadorConMayorCantidadRobosTotales")
    print("14. MostrarJugadorConMayorCantidadBloqueosTotales")
    print("15. MostrarJugadoresConMayorPorcentajeDeTirosLibresIngresado")
    print("16. MostrarJugadoresConMayorPorcentajeDeTirosXPartidoExcluyendoAlUltimo")
    print("17. MostrarJugadorConMayorCantidadLogros")
    print("18. MostrarJugadoresConMayorPorcentajeDeTirosTriplesIngresado")
    print("19. MostrarJugadorConMayorCantidadTempJugadas")
    print("20. MostrarJugadorConMayorPorcentajeTiroDeCampo")
    print("0. SALIR")

    opcion = int(input("Ingese Opcion: "))

    if (opcion == 1):
        os.system('cls')
        print(MostrarJugadores(listaJugadores))
        limpiarConsola()

    elif (opcion == 2):
        os.system('cls')
        print(MostrarJugadorEspecifico(listaJugadores))
        limpiarConsola()

    elif (opcion == 3):
        pass

    elif (opcion == 4):
        os.system('cls')
        print(SeleccionarJugador(listaJugadores))
        nombre = input("Nombre: ")
        print(BuscarJugador(nombre))
        limpiarConsola()

    elif (opcion == 5):
        os.system('cls')
        print(CalcularMostrarPromedioPuntosXPartidoDeTodoEquipo(listaJugadores))
        limpiarConsola()

    elif (opcion == 6):
        os.system('cls')
        if MostrarJugadorPerteneceAlSalonDeLaFama(listaJugadores):
            print("Pertenece")
        else:
            print("NO Pertenece")
        limpiarConsola()

    elif (opcion == 7):
        os.system('cls')
        print(MostrarJugadorConMayorCantidadRebotesTotales(listaJugadores))
        limpiarConsola()

    elif (opcion == 8):
        os.system('cls')
        print(MostrarJugadorConMayorPorcentajeDeTirosDeCampo(listaJugadores))
        limpiarConsola()

    elif (opcion == 9):
        os.system('cls')
        print(MostrarJugadorConMayorCantidadAsistenciasTotales(listaJugadores))
        limpiarConsola()

    elif (opcion == 10):
        os.system('cls')
        MostrarJugadoresConMayorPuntosIngresado(listaJugadores)
        limpiarConsola()

    elif (opcion == 11):
        os.system('cls')
        MostrarJugadoresConMayorRebotesIngresado(listaJugadores)
        limpiarConsola()

    elif (opcion == 12):
        os.system('cls')
        MostrarJugadoresConMayorAsistenciasIngresado(listaJugadores)
        limpiarConsola()

    elif (opcion == 13):
        os.system('cls')
        print(MostrarJugadorConMayorCantidadRobosTotales(listaJugadores))
        limpiarConsola()

    elif (opcion == 14):
        os.system('cls')
        print(MostrarJugadorConMayorCantidadBloqueosTotales(listaJugadores))
        limpiarConsola()

    elif (opcion == 15):
        os.system('cls')
        MostrarJugadoresConMayorPorcentajeDeTirosTriplesIngresado(
            listaJugadores)
        limpiarConsola()

    elif (opcion == 16):
        os.system('cls')
        print(MostrarJugadoresConMayorPorcentajeDeTirosXPartidoExcluyendoAlUltimo(
            listaJugadores))
        limpiarConsola()

    elif (opcion == 17):
        os.system('cls')
        print(MostrarJugadorConMayorCantidadLogros(listaJugadores))
        limpiarConsola()

    elif (opcion == 18):
        os.system('cls')
        MostrarJugadoresConMayorPorcentajeDeTirosTriplesIngresado
        limpiarConsola()

    elif (opcion == 19):
        os.system('cls')
        print(MostrarJugadorConMayorCantidadTempJugadas(listaJugadores))
        limpiarConsola()

    elif (opcion == 20):
        os.system('cls')
        MostrarJugadorConMayorPorcentajeTiroDeCampo(listaJugadores)
        limpiarConsola()

    elif (opcion == "0"):
        break

    else:
        print("Ingrese opcion correcta")
