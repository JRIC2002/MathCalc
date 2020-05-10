#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#[*] Name of the tool: MathCalc
#[*] Description: Solve math operations.
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
        print("         {} __  __       _   _        {}____      _".format(color.blue, color.green))
        print("         {}|  \/  | __ _| |_| |__    {}/ ___|__ _| | ___".format(color.blue, color.green))
        print("         {}| |\/| |/ _` | __| '_ \  {}| |   / _` | |/ __|".format(color.blue, color.green))
        print("         {}| |  | | (_| | |_| | | | {}| |__| (_| | | (__".format(color.blue, color.green))
        print("         {}|_|  |_|\__,_|\__|_| |_|  {}\____\__,_|_|\___| {}v1.0".format(color.blue, color.green, color.white))
        print("")
        print("               {}</> {}Tool coded by:{} JRIC2002 {}</>{}".format(color.gray, color.yellow, color.white, color.gray, color.white))
        print("          {}</> {}Description:{} Solve math operations {}</>{}".format(color.gray, color.yellow, color.white, color.gray, color.white))
        print("")

    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta MathCalc. """

        print("{}Usage: python3 MathCalc.py [options]".format(color.white))
        print("")
        print("Options:")
        print("   -h, --help              Show this help message and exit.")
        print("   -v, --version           Show program's version number and exit.")
        print("")
        print("   Basic operations:")
        print("      At least one of these options must be provided to perform the mathematical operation.")
        print("")
        print("      -s, --sum               Perform the mathematical operation of 'SUM'")
        print("      -r, --subtract          Perform the mathematical operation of 'SUBTRACT'")
        print("      -m, --multiply          Perform the mathematical operation of 'MULTIPLY'")
        print("      -d, --divide            Perform the mathematical operation of 'DIVIDE'")
        print("      -p, --power             Perform the mathematical operation of 'POWER'")

    def version(self):
        """ Imprime la versión de la herramienta MathCalc. """

        print("{}#MathCalc version 1.0".format(color.white))

    def error1(self):
        """ Imprime un mensaje de error. """

        print("{}Usage: python3 MathCalc.py [options]".format(color.white))
        print("")
        print("MathCalc.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.")

    def error2(self):
        """ Imprime un mensaje de error de argumentos. """

        print("{}Usage: python3 MathCalc.py [options]".format(color.white))
        print("")
        print("MathCalc.py: Error: Invalid option or arguments.")
        print("Use -h or --help to see the help menu.")

#Instancia de la clase Start
start = Start()

#START
if len(sys.argv) == 1:
    start.logo()
    start.help_menu()
elif len(sys.argv) == 2:
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        start.logo()
        start.help_menu()
    elif sys.argv[1] == "-v" or sys.argv[1] == "--version":
        start.version()
    else:
        start.logo()
        start.error1()
else:
    if sys.argv[1] == "-s" or sys.argv[1] == "--sum":
        functions.sum(sys.argv[2:])
    elif sys.argv[1] == "-r" or sys.argv[1] == "--subtract":
        functions.subtract(sys.argv[2:])
    elif sys.argv[1] == "-m" or sys.argv[1] == "--multiply":
        functions.multiply(sys.argv[2:])
    elif len(sys.argv) == 4:
        if sys.argv[1] == "-d" or sys.argv[1] == "--divide":
            functions.divide(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "-p" or sys.argv[1] == "--power":
            functions.power(sys.argv[2], sys.argv[3])
        else:
            start.logo()
            start.error1()
    else:
        start.logo()
        start.error2()
