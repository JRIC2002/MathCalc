#!/usr/bin/python3
# -*- coding: utf-8 -*-

#[*] Name of the tool: MathCalc
#[*] Description: Solve math operations.
#[*] Version: 1.1
#[*] Author: JRIC2002
#[*] Date of creation: 04/05/2020

#Modules

#External modules
import sys

#Internal modules
from modules import functions

class Color:
    """ Colores en código ANSI. """

    #Foreground
    blackColor = "\033[0;30m"
    grayColor = "\033[1;30m"
    redColor = "\033[1;31m"
    greenColor = "\033[1;32m"
    yellowColor = "\033[1;33m"
    blueColor = "\033[1;34m"
    purpleColor = "\033[1;35m"
    cyanColor = "\033[1;36m"
    whiteColor = "\033[1;37m"
    resetColor = "\033[0;0m"

    #Background
    blackBackColor = "\033[0;40m"
    grayBackColor = "\033[1;40m"
    redBackColor = "\033[1;41m"
    greenBackColor = "\033[1;42m"
    yellowBackColor = "\033[1;43m"
    blueBackColor = "\033[1;44m"
    purpleBackColor = "\033[1;45m"
    cyanBackColor = "\033[1;46m"
    whiteBackColor = "\033[1;47m"
    resetBackColor = "\033[0;0m"

#Instancia de la clase Color
color = Color()

class Start:
    """ Inicio de la herramienta MathCalc. """
    
    def __init__(self):
        """ Variables de instancia. """
        pass

    def logo(self):
        """ Imprime el logo de la herramienta MathCalc. """

        print("")
        print("         {} __  __       _   _        {}____      _".format(color.blueColor, color.greenColor))
        print("         {}|  \/  | __ _| |_| |__    {}/ ___|__ _| | ___".format(color.blueColor, color.greenColor))
        print("         {}| |\/| |/ _` | __| '_ \  {}| |   / _` | |/ __|".format(color.blueColor, color.greenColor))
        print("         {}| |  | | (_| | |_| | | | {}| |__| (_| | | (__".format(color.blueColor, color.greenColor))
        print("         {}|_|  |_|\__,_|\__|_| |_|  {}\____\__,_|_|\___| {}v1.1".format(color.blueColor, color.greenColor, color.whiteColor))
        print("")
        print("               {}</> {}Tool coded by:{} JRIC2002 {}</>{}".format(color.grayColor, color.yellowColor, color.whiteColor, color.grayColor, color.whiteColor))
        print("          {}</> {}Description:{} Solve math operations {}</>{}".format(color.grayColor, color.yellowColor, color.whiteColor, color.grayColor, color.resetColor))
        print("")

    def help_menu(self):
        """ Imprime el menú de ayuda de la herramienta MathCalc. """

        print("{}Usage: python3 MathCalc.py [options]".format(color.whiteColor))
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
        print("{}".format(color.resetColor))

    def version(self):
        """ Imprime la versión de la herramienta MathCalc. """

        print("{}#MathCalc version 1.1{}".format(color.whiteColor, color.resetColor))

    def error1(self):
        """ Imprime un mensaje de error. """

        print("{}Usage: python3 MathCalc.py [options]".format(color.whiteColor))
        print("")
        print("MathCalc.py: Error: Invalid option.")
        print("Use -h or --help to see the help menu.{}".format(color.resetColor))

    def error2(self):
        """ Imprime un mensaje de error de argumentos. """

        print("{}Usage: python3 MathCalc.py [options]".format(color.whiteColor))
        print("")
        print("MathCalc.py: Error: Invalid option or arguments.")
        print("Use -h or --help to see the help menu.".format(color.resetColor))

#Instancia de la clase Start
start = Start()

#Start
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
