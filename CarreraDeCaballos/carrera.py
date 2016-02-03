#!/usr/bin/env python3
#coding=utf-8

""" 
    Carrera de caballos donde en cada turno cada caballo avanza un número 
    aleatorio de pasos. Determinar el ganador.
"""

__author__      = "Carlos A. Gómez Urda"
__copyright__   = "Copyright 2016"
__credits__     = ["Carlos A. Gómez Urda"]
__license__     = "GPL"
__version__     = "1.1"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "03/02/2016"


import random, time

def llegoAMeta( caballo, pasosMeta):
    """
    Comprobar si un caballo ha llegado a la meta. El estado resultante se 
    almacena en el caballo.
    @param caballo Caballo a comprobar si llegó a meta.
    @param pasosMeta Pasos donde está la línea de meta.
    @return True/False si llegó a la meta.
    """
    if caballo["pasos"] >= pasosMeta:
        caballo["meta"] = True
    return caballo["meta"]


def avanzarTurno( caballo, pasosMaximos):
    """
    Avanzar un caballo un número de pasos en un turno.
    @param caballo Caballo que avanzará pasos en el turno.
    @param pasos Pasos máximos posibles en un turno.
    """
    caballo["pasos"] += random.randrange( pasosMaximos+1)


def mostrarCarrera( caballo1, caballo2, pasosMeta):
    """
    Visualizar el estado actual de la carrera.
    @param caballo1 Caballo 1.
    @param caballo2 Caballo 2.
    @param pasosMeta Pasos donde se encuentra la línea de meta.
    """
    print( "%10s: %s" % (caballo1["nombre"][:10], "="*caballo1["pasos"]))
    print( "%10s: %s" % (caballo2["nombre"][:10], "="*caballo2["pasos"]))
    print( "%10s:%s" % ("Meta", " "*pasosMeta + "|"))
    



PASOS_META = 80
MAX_PASOS_POR_TURNO = PASOS_META // 10
caballo1 = {"nombre": "C1", "pasos": 0, "meta": False}
caballo2 = {"nombre": "C2", "pasos": 0, "meta": False}

print( "######### CARRERA DE CABALLOS PYTHON #########\n")

nombre = input( "Nombre del Caballo 1: ").strip()
if nombre: caballo1['nombre'] = nombre
nombre = input( "Nombre del Caballo 2: ").strip()
if nombre: caballo2["nombre"] = nombre

pasosMeta = PASOS_META

while True:
    pasos = input("Pasos línea de meta [%d]: " % PASOS_META).strip()
    if not pasos: break
    try:
        pasosMeta = int( pasos)
    except:
        print( "Tienes que introducir un número.")
        continue
    if pasosMeta > 0: break
    print( "El número de pasos como final de carrera debe ser > 0")

while True:    
    pasos = input( "Pasos máximos por turno [0 aleatorio]: ").strip()
    if not pasos or pasos == "0": 
        pasosMaxPorTurno = random.randint( 1, pasosMeta)
        break
    try:
        pasosMaxPorTurno = int( pasos)
    except:
        print( "Tienes que introducir un número")
        continue
    if pasosMaxPorTurno > 0 and pasosMaxPorTurno <= pasosMeta: break
    print( "Error: El número de pasos debe estar en [0,%d]" % pasosMeta)
    
print( "\nNúmero de pasos máximo por turno: %d" % pasosMaxPorTurno)
print( "Número de pasos para llegar a meta: %d\n" % pasosMeta)
input( "\nPulsa cualquier tecla para continuar...\n")
print( "La carrera comienza en...")
for i in [3, 2, 1, "¡YA!\n"]:
    time.sleep( 1);
    print( i)
print()

while True:
    time.sleep(1)
    avanzarTurno( caballo1, pasosMaxPorTurno)
    avanzarTurno( caballo2, pasosMaxPorTurno)
    mostrarCarrera( caballo1, caballo2, pasosMeta)
    if llegoAMeta( caballo1, pasosMeta) | llegoAMeta( caballo2, pasosMeta): 
        break

print()
if caballo1["meta"] and caballo2["meta"]: 
    print( "EMPATE")
else:
    ganador = caballo1["nombre"] if caballo1["meta"] else caballo2["nombre"]
    print( "GANADOR CABALLO %s" % ganador)

