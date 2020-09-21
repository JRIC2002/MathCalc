#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" Este módulo contiene funciones que realizan operaciones matemáticas. """

__author__ = "JRIC2002"
__copyright__ = "Copyright 2020, JRIC2002"
__credits__ = "JRIC2002"
__license__ = "GNU General Public License v3.0"
__version__ = "1.1"
__maintainer__ = "JRIC2002"
__email__ = "example@gmail.com"
__status__ = "Production"

def sum(numbers):
    """ Imprime el resultado de la suma. """

    try:
        result = 0
        for number in numbers:
            result = result + float(number)
        print(result)
    except Exception:
        print("Error: No se puede sumar letras o símbolos.")

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
        print("Error: No se puede restar letras o símbolos.")

def multiply(numbers):
    """ Imprime el resultado de la multiplicación. """

    try:
        result = 1
        for number in numbers:
            result = result * float(number)
        print(result)
    except Exception:
        print("Error: No se puede multiplicar letras o símbolos.")

def divide(num1, num2):
    """ Imprime el resultado de la división. """
    
    try:
        if float(num2) != 0:
            print(float(num1) / float(num2))
        else:
            print("Error: No se puede dividir entre cero.")
    except Exception:
        print("Error: No se puede dividir letras o símbolos.")

def power(num1, num2):
    """ Imprime el resultado de la potencia. """

    try:
        print(float(num1) ** float(num2))
    except Exception:
        print("Error: La base y el exponente no pueden ser letras o símbolos.")

#Start
if __name__ == "__main__":
    print("Este archivo es un módulo...")
