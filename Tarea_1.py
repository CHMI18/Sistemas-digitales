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
        return num
    else:
        resto = num % b
        parte_entera = int(num/b)
        x = [resto]
        return x.extend(dividir_por(parte_entera, b))

def num_a_base_10(x, A):
    if float_check(x):
        pass

    else:
        pass
    