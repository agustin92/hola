# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

x = np.linspace(0,10,100)
frec= 1
ph = 0 
am = 10

def coseno(x,f,p,a):
    res = []
    long = len(x)
    i=0
    while i<long:
        resaux = a*mt.cos(f*x[i]+p)
        res.append(resaux)
        i = i + 1
    return res