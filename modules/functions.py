#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

""" Funciones aritmeticas. """

__author__ = "JRIC2002"
__copyright__ = "Copyright 2020, JRIC2002"
__credits__ = "JRIC2002"
__license__ = "GNU General Public License v3.0"
__version__ = "1.0"
__maintainer__ = "JRIC2002"
__email__ = "joselito18032002@gmail.com"
__status__ = "Production"

def sum(numbers):
    """ Imprime el resultado de la suma. """

    try:
        result = 0
        for number in numbers:
            result = result + float(number)
        print(result)
    except Exception:
        print("Error: no se puede sumar letras o simbolos.")

def subtract(numbers):
    """ Imprime el resultado de la resta. """

    try:
        result = 0
        i = 1
        while i < len(numbers):
            result = result + float(numbers[i])
            i = i + 1
        result = float(numbers[0]) - result
        print(result)
    except Exception:
        print("Error: no se puede restar letras o simbolos")

def multiply(numbers):
    """ Imprime el resultado de la multiplicación. """

    try:
        result = 1
        for number in numbers:
            result = result * float(number)
        print(result)
    except Exception:
        print("Error: no se puede multiplicar letras o simbolos")

def divide(num1, num2):
    """ Imprime el resultado de la división. """
    
    try:
        print(float(num1) / float(num2))
    except Exception:
        print("Error: no se puede dividir letras o simbolos")

def power(num1, num2):
    """ Imprime el resultado de la potencia. """

    try:
        print(float(num1) ** float(num2))
    except Exception:
        print("Error: no se puede tener como base o exponente letras o simbolos")

#START
if __name__ == "__main__":
    print("Este archivo es un módulo...")
