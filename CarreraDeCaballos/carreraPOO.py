#!/usr/bin/env python3
#coding=utf-8

""" 
    Carrera de caballos donde en cada turno cada caballo avanza un número 
    aleatorio de pasos. Implementado con paradigma POO.
"""

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.2"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "04/02/2016"


import random, time

class ArgumentoException( Exception):
    """
    Excepción a ser lanzadas por error en los argumentos de llamada a una
    función o método.
    """
    pass


class Caballo:
    """
    Caballo de carreras.
    """

    __MAX_PASOS_POR_TURNO = 10
  
 
    def __init__( self, nombre = None, maxPasosPorTurno = None):
        """
        Constructor.
        @param nombre Nombre del caballo.
        @param maxPasosPorTurno Máximo de pasos que puede alcanzar en un turno.
        """
        self.nombre = nombre
        self.maxPasosPorTurno = maxPasosPorTurno
        self.__carreras = []
        self.__pasosCarreraActual = 0


    def __str__( self):
        """
        Equivalente a toString(). Representar el objeto como una cadena.
        """
        return self.nombre


    def MAX_PASOS_POR_TURNO():
        """
        Obtenertener el valor por defecto del número máximo de pasos por turno 
        que puede dar un caballo.
        @return Valor por defecto de número máximo de pasos por turno.
        """
        return Caballo.__MAX_PASOS_POR_TURNO


    @property
    def nombre( self):
        """
        Obtener el nombre del Caballo.
        @return Nombre del caballo.
        """
        return self.__nombre


    @nombre.setter
    def nombre( self, nombre = None):
        """
        Cambiar el nombre del caballo.
        @param nombre Nuevo nombre del caballo
        """
        if nombre is None:
            self.__nombre = "<Sin Nombre>"
        
        nombre = str( nombre).strip()
        self.__nombre = "<Sin nombre>" if not nombre else nombre 


    @property
    def maxPasosPorTurno( self):
        """
        Obtener el número máximo de pasos por turno que puede dar el caballo.
        @return Número de pasos máximo.
        """
        return self.__maxPasosPorTurno


    @maxPasosPorTurno.setter
    def maxPasosPorTurno( self, maxPasos = None):
        """
        Cambiar el número de pasos máximos por turno que puede dar el caballo.
        @param maxPasos Nuevo número máximo de pasos por turno.
        """
        if not maxPasos:
            self.__maxPasosPorTurno = Caballo.__MAX_PASOS_POR_TURNO
            return

        try:
            maxPasos = int( maxPasos)
        except ValueError as e:
            print( e)
            raise ArgumentoException( "Argumento maxPasos inválido.")

        if maxPasos < 1:
            raise ArgumentoException( "Argumento maxPasos < 1.")

        self.__maxPasosPorTurno = maxPasos


    @property
    def pasosCarreraActual( self):
        """
        Obtener el número de pasos realizados hasta ahora en la carrera actual.
        @return Número de pasos recorridos.
        """
        return self.__pasosCarreraActual


    def inscribirCarrera( self, carrera):
        """ 
        Añadir una carrera a las carreras en las cuales el caballo ha 
        participado.
        @param carrera Carrera a incluir.
        """
        if carrera is None:
            raise ArgumentoException( "Error en el argumento carrera (None).")

        if carrera in self.__carreras:
            raise ArgumentoException( "Ya se ha inscrito en esa carrera.")

        self.__carreras.append( carrera)
        self.__pasosCarreraActual = 0


    def avanzarPasos( self):
        """
        Avanzar un número de pasos en un turno en la carrera actual. 
        """
        self.__pasosCarreraActual += random.randrange( self.maxPasosPorTurno+1)



class Carrera:
    """
    Carrera de Caballos.
    """
    
    __PASOS_META = 80

    def __init__( self, pasosMeta = None, nombre = None):
        """
        Constructor.
        @parama pasosMeta Pasos donde se encuentra la línea de meta.
        """
        self.pasosMeta = pasosMeta
        self.nombre = nombre
        self.__caballos = dict()
        self.__ganadores = []


    def PASOS_META():
        """
        Obtener el valor de pasos de la línea de meta a asignar por defecto.
        @return Pasos de la línea de meta por defecto.
        """
        return Carrera.__PASOS_META


    @property
    def nombre( self):
        """
        Obtener el nombre del Caballo.
        @return Nombre del caballo.
        """
        return self.__nombre


    @nombre.setter
    def nombre( self, nombre = None):
        """
        Cambiar el nombre de la carrera.
        @param nombre Nuevo nombre de la carrera
        """
        if nombre is None:
            self.__nombre = "<Sin Nombre>"
        
        nombre = str( nombre).strip()
        self.__nombre = "<Sin nombre>" if not nombre else nombre 


    @property
    def pasosMeta( self):
        """
        Obtener el número de pasos donde se encuentra la línea de meta.
        @return Número de pasos de meta.
        """
        return self.__pasosMeta


    @pasosMeta.setter
    def pasosMeta( self, pasosMeta = None):
        """
        Cambiar el número de pasos donde se encuentra la línea de meta.
        @param pasosMeta Nuevo número de pasos de la línea de meta.
        """
        if not pasosMeta:
            self.__pasosMeta = Carrera.__PASOS_META
            return

        try:
            pasosMeta = int( pasosMeta)
        except ValueError as e:
            print( e)
            raise ArgumentoException( "Argumento pasosMeta inválido.")

        if pasosMeta < 1:
            raise ArgumentoException( "Argumento pasosMeta < 1.")

        self.__pasosMeta = pasosMeta

  
    @property
    def ganadores( self):
        """
        Obtener los ganadores de la carrera
        @return Tupla con los ganadores.
        """
        return tuple( self.__ganadores)


    def numeroDeInscritos( self):
        """
        Devolver el número de caballos inscritos en la carrera.
        @return Número de caballos inscritos.
        """
        return len( self.__caballos)


    def visualizarTurno( self):
        """
        Visualizar el estado actual de la carrera.
        """
        for caballo, datos in self.__caballos.items():
            print( "%2d-%12s: %s" % 
                   (datos["dorsal"], caballo.nombre[:12], "="*datos["pasos"]))

        print( "%15s:%s" % ("Meta", " "*self.__pasosMeta + "|"))
            

    def registrarCaballo( self, caballo):
        """
        Registrar un caballo que va a participar en la carrera.
        @param caballo Caballo a registrar.
        """
        if caballo is None:
            raise ArgumentoException( "Argumento caballo inválido (None).")
        
        if caballo in self.__caballos: 
            raise ArgumentoException( "El caballo ya está inscrito.")

        self.__caballos[caballo] = {"pasos": 0, "puesto": None,
                                    "dorsal": self.numeroDeInscritos()+1}
        caballo.inscribirCarrera( self)


    def avanzarTurno( self):
        """
        Avanzar un turno en todos los caballos participantes en la carrera.
        @return True si hay ganador, False si no ha finalizado la carrera.
        """
        esFinalDeCarrera = False
        for caballo, datos in self.__caballos.items():
            caballo.avanzarPasos()
            datos["pasos"] = caballo.pasosCarreraActual
            if (not esFinalDeCarrera and
                caballo.pasosCarreraActual >= self.pasosMeta):
                esFinalDeCarrera = True
        return esFinalDeCarrera


    def calcularPuestos( self):
        """
        Calcular los puestos de los caballos en la clasificación resultante de
        la carrera. También guarda los ganadores de la carrera.
        MEJORA: Considerar si la carrera ha finalizado o no para calcular los
        puestos durante la carrera sin ganadores, o al final de la carrera.
        """
        self.__clasificacion = sorted(self.__caballos.items(), 
                                      key=lambda x: x[1]["pasos"], reverse=True)
        puesto = 1
        pasosAnterior = self.__clasificacion[0][1]["pasos"]
        for caballo, datos in self.__clasificacion:
           if datos["pasos"] < pasosAnterior:
                puesto += 1
                pasosAnterior = datos["pasos"]
           elif puesto == 1: self.__ganadores.append( caballo)
           datos["puesto"] = puesto
            

    def puestoAlcanzado( self, caballo):
        """
        Obtener el puesto en el cual un caballo quedó en la carrera.
        @param caballo Caballo a conocer su puesto final en la carrera.
        @return Puesto en que quedó o None si la carrera no ha finalizado.
        """
        if caballo not in self.__caballos:
            raise ArgumentoException( "El caballo no participó en la carrera.")

        return self.__caballos[caballo]["puesto"]
        

    def esGanador( self, caballo):
        """
        Informar si un caballo ganó la carrera.
        @param caballo Caballo a saber si ganó la carrera.
        @return True o False si ganó o no la carrera.
        """
        if caballo not in self.__caballos:
            raise ArgumentoException( "El caballo no participó en la carrera.")

        return caballo in self.__ganadores


    def mostrarClasificacion( self):
        """
        Visualizar la clasificación de la carrera. Antes se ha debido llamar a
        calcularPuestos.
        """
        print( "\n**** CLASIFICACIÓN DE LA CARRERA %s ****" % self.nombre)
        for caballo, datos in self.__clasificacion:
            print( "%dº.- Dorsal %2d | %20s | Pasos %d" % 
                   (datos["puesto"], datos["dorsal"], caballo.nombre, 
                    datos["pasos"]))
     


print( "#########  CARRERA DE CABALLOS PYTHON  #########\n")

while True:
    nombre = input( "\nIntroduce el nombre de la carrera: ")
    pasos = input( "Pasos línea de meta [%d]: " % Carrera.PASOS_META())
    try:
        carrera = Carrera( pasos, nombre)
    except ArgumentoException as e:
        print( e)
        print( "Introduce los datos de la carrera correctamente.")
        continue
    break

while True:
    numeroDeCaballos = input( "\nIntroduce el número de caballos: ")
    if not numeroDeCaballos.strip(): continue
    try:
        numeroDeCaballos = int( numeroDeCaballos)
    except ValueError as e:
        print( e)
        print( "Debes introducir un número de caballos participantes.")
        continue
    if numeroDeCaballos > 1: break

    print( "Debes introducir al menos dos caballos.")

for i in range( numeroDeCaballos):
    while True:
        print( "\nIntroduce los datos del Caballo %d" % (i+1))
        nombre = input( "\tNombre: ")
        maxPasos = input( "\tPasos máximos por turno [%d]: " % 
                          Caballo.MAX_PASOS_POR_TURNO())
        try:
            caballo = Caballo( nombre, maxPasos)
        except ArgumentoException as e:
            print( e)
            print( "Introduce los datos del caballo correctamente")
            continue
        break
    carrera.registrarCaballo( caballo)

input( "\nPulsa cualquier tecla para continuar...\n")
print( "La carrera comienza en...")
for i in [3, 2, 1, "¡YA!\n"]:
    time.sleep( 1)
    print( i)
print()

esFinalDeCarrera = False
while not esFinalDeCarrera: 
    time.sleep(1)
    esFinalDeCarrera = carrera.avanzarTurno()
    carrera.visualizarTurno()
    
carrera.calcularPuestos()
carrera.mostrarClasificacion()
print( "Ganadores: " + str( [caballo.nombre for caballo in carrera.ganadores]))



