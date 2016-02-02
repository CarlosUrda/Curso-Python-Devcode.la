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
__version__     = "1.0"
__maintainer__  = "Carlos A. Gómez Urda"
__email__       = "carlosurda@yahoo.es"
__status__      = "Producción"
__date__        = "02/02/2016"


import random, time

PASOS_META = 80
MAX_PASOS_POR_TURNO = PASOS_META // 10

print( "#### CARRERA DE CABALLOS PYTHON ####")

pasosMeta = PASOS_META
pasosMaxPorTurno = MAX_PASOS_POR_TURNO

while True:    
    pasos = input( "Pasos máximos por turno [0 aleatorio]: ").strip()
    if not pasos: break
    try:
        pasosMaxPorTurno = int( pasos)
    except:
        print( "Tienes que introducir un número")
        continue

    if pasosMaxPorTurno > 0: break
    elif pasosMaxPorTurno ==  0:
        pasosMaxPorTurno = random.randint( 1, MAX_PASOS_POR_TURNO)
        break
    print( "Error: El número de pasos debe ser positivo")
    
while True:
    pasos = input("Pasos línea de meta [%d]: " % PASOS_META).strip()
    if not pasos: break
    try:
        pasosFinalCarrera = int( pasos)
    except:
        print( "Tienes que introducir un número.")
        continue
    if pasosFinalCarrera > 0: break
    print( "El número de pasos como final de carrera debe ser > 0")

print( "Número de pasos máximo por turno: %d" % pasosMaxPorTurno)
print( "Número de pasos para llegar a meta: %d\n" % pasosFinalCarrera)
print( "La carrera comienza en:", end=" ")
for i in [3, 2, 1, "¡YA!"]:
#    time.sleep( 2);
    print( i, end=" ")

print()
pasosCaballo1 = pasosCaballo2 = 0

while True:
#    time.sleep(1)
    pasosCaballo1 += int( random.random() * pasosMaxPorTurno) + 1
    pasosCaballo2 += int( random.random() * pasosMaxPorTurno) + 1
    print( "Caballo1: " + "="*pasosCaballo1)
    print( "Caballo2: " + "="*pasosCaballo2)
    print( "Meta:    " + " "*pasosFinalCarrera + "|")
    if max( pasosCaballo1, pasosCaballo2) >= pasosFinalCarrera: break

if pasosCaballo1 == pasosCaballo2: print( "EMPATE")
else: print( "GANADOR CABALLO %d" % (1 if pasosCaballo1 > pasosCaballo2 else 2))

