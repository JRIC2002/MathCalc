#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#[*] Name of the tool: MathCalc
#[*] Description:
#[*] Version: 1.0
#[*] Author: JRIC2002
#[*] Date of creation: 04/05/2020
#[*] Date of last update: 04/05/2020

#MODULES

#External modules
import sys

#Internal modules
from modules import functions

class Color:
    """ Colores en código ANSI. """

    #Foreground
    black = "\033[0;30m"
    gray = "\033[1;30m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    magenta = "\033[1;35m"
    cyan = "\033[1;36m"
    white = "\033[1;37m"

    #Background
    b_black = "\033[0;40m"
    b_gray = "\033[1;40m"
    b_red = "\033[1;41m"
    b_green = "\033[1;42m"
    b_yellow = "\033[1;43m"
    b_blue = "\033[1;44m"
    b_magenta = "\033[1;45m"
    b_cyan = "\033[1;46m"
    b_white = "\033[1;47m"

#Instancia de la clase Color
color = Color()

class Start():
    """ Inicio de la herramienta MathCalc. """
    
    def __init__(self):
        """ Variables de instancia. """
        pass

    def logo(self):
        """ Imprime el logo de la herramienta MathCalc. """

        print("")
        print("          __  __       _   _        ____      _")
        print("         |  \/  | __ _| |_| |__    / ___|__ _| | ___")
        print("         | |\/| |/ _` | __| '_ \  | |   / _` | |/ __|")
        print("         | |  | | (_| | |_| | | | | |__| (_| | | (__")
        print("         |_|  |_|\__,_|\__|_| |_|  \____\__,_|_|\___| v1.0")

#Instancia de la clase Start
start = Start()

#START
if len(sys.argv) == 1:
    start.logo()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        pass
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        pass
    else:
        pass
else:
    if sys.argv[1] == "-s":
        functions.addition(sys.argv[2:])
    elif sys.argv[1] == "-r":
        functions.subtraction(sys.argv[2:])
    elif sys.argv[1] == "-m":
        functions.multiplication(sys.argv[2:])
    elif len(sys.argv) == 4:
        if sys.argv[1] == "-d":
            functions.division(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "-p":
            functions.power(sys.argv[2], sys.argv[3])
        else:
            print("ERROR de opcion")
    else:
        print("Error de opcion o de argumentos")
