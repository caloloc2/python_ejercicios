import random
from matplotlib import pyplot
import numpy as np
import math

d = 9 # numero de direcciones (10)
angulos = np.arange(0, 360, 36) # rango de angulos definidos
x = np.zeros(d) # arreglo para componentes x
y = np.zeros(d) # arreglo para componentes y

for i in range(d):
    np.random.seed(1492) # se define semilla
    r = random.randint(1, 12) # aleatorio lanzamiento dos dados
    a = random.randint(0, 9) # aleatorio numero angulo
    rad = (a*math.pi)/180 # convierte angulo a radianes
    x[i] = r * math.cos(rad) # obtiene la componente x 
    y[i] = r * math.sin(rad) # obtiene la componente y

pyplot.plot(x, y) # grafica las coordenadas obtenidas
pyplot.show() # muestra la ventana
