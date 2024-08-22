import numpy as np
import soundfile as sf


#La función revisa si es que el número a trabajar es o no un float al mirar si tiene o no un punto

def float_check(x):
    x = str(x)
    if '.' in x:
        return True
    else:
        return False


#Divide de forma recursiva para encontrar la representación en base b de un número de base 10

def dividir_por(num, b):
    if num < b:
        return [num]
    else:
        resto = num % b
        parte_entera = int(num/b)
        x = [resto]
        return x.extend(dividir_por(parte_entera, b))


#Obtiene un número num con base a, devuelve un número equivalente en base 10
def base10(num, a):
    if float_check(num):
        num = str(num)
        num = num.split('.')
        entero, decimal = num[0], num[1]
        total = 0
        for i in range(len(entero)):
            total += num[-(i + 1)] * (a**i)

        for i in range(len(decimal)):
            total += num[i] * (a**(-(i + 1)))
        return total
        
    else:
        num = str(num)
        total = 0
        for i in range(len(num)):
            total += num[-(i + 1)] * (a**i)
        return total
            
            
