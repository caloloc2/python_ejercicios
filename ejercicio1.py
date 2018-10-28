import tkinter as tk
import random

from random import shuffle
import numpy as np
import matplotlib.pyplot as plt

# Calculo de cuantos click en promedio daria hasta perder
prob = [2/16]
pb = 1
for n in range(0,14):
    pb *= (14-n)/(16-n)
    pn = 2/(16-(n+1))
    prob += [pb * pn]

x = np.array([i+1 for i in range(15)])
px = np.array(prob)
mx = np.sum(x*px)
vx = np.sum((x**2)*px) - mx**2
sx = np.sqrt(vx)

#plt.bar(x, px) # en caso de querer graficar los calculos
#plt.show() # muestra la grafica
print ("Clicks en promedio que puede dar hasta perder: ", mx)

# contador click
click = 0
# posiciones de los casilleros negros
negras= [2, 4, 7, 9, 21, 22, 24, 26, 28, 38, 40, 44, 47, 53, 57, 58]
# obtiene dos numeros randomicos que corresponden a las minas (posicion)
mina1 = r = random.randint(0, 15)
mina2 = r = random.randint(0, 15)

def write_slogan(num):
    global click
    if (negras[mina1]==num):
        print("Encontro la Mina 1 al "+repr(click)+" click!!! Perdio.")
    elif (negras[mina2]==num):
        print("Encontro la Mina 2 al "+repr(click)+" click!!! Perdio.")
    else:        
        if (num==2):
            b0.config(bg = "white")
        elif (num==4):
            b1.config(bg = "white")
        elif (num==7):
            b2.config(bg = "white")
        elif (num==9):
            b3.config(bg = "white")
        elif (num==21):
            b4.config(bg = "white")
        elif (num==22):
            b5.config(bg = "white")
        elif (num==24):
            b6.config(bg = "white")
        elif (num==26):
            b7.config(bg = "white")
        elif (num==28):
            b8.config(bg = "white")
        elif (num==38):
            b9.config(bg = "white")
        elif (num==40):
            b10.config(bg = "white")
        elif (num==44):
            b11.config(bg = "white")
        elif (num==47):
            b12.config(bg = "white")
        elif (num==53):
            b13.config(bg = "white")
        elif (num==57):
            b14.config(bg = "white")
        elif (num==58):
            b15.config(bg = "white")
    click+=1

# configuracion de ventana
root = tk.Tk()
root.geometry("250x250")
frame = tk.Frame(root)
frame.pack()

#creacion de matriz de botones
i=0
fila = 30
for f in range(8):
    columna = 1
    for c in range(8): 
        # botones negros
        if (i==2):
            b0 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b0.grid(row=fila, column=columna)
        elif (i==4):
            b1 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b1.grid(row=fila, column=columna)
        elif (i==7):
            b2 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b2.grid(row=fila, column=columna)
        elif (i==9):
            b3 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b3.grid(row=fila, column=columna)
        elif (i==21):
            b4 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b4.grid(row=fila, column=columna)
        elif (i==22):
            b5 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b5.grid(row=fila, column=columna)
        elif (i==24):
            b6 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b6.grid(row=fila, column=columna)
        elif (i==26):
            b7 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b7.grid(row=fila, column=columna)
        elif (i==28):
            b8 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b8.grid(row=fila, column=columna)
        elif (i==38):
            b9 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b9.grid(row=fila, column=columna)
        elif (i==40):
            b10 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b10.grid(row=fila, column=columna)
        elif (i==44):
            b11 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b11.grid(row=fila, column=columna)
        elif (i==47):
            b12 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b12.grid(row=fila, column=columna)
        elif (i==53):
            b13 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b13.grid(row=fila, column=columna)
        elif (i==57):
            b14 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b14.grid(row=fila, column=columna)
        elif (i==58):
            b15 = tk.Button(frame, width=2, height=1, bg = "black", command = lambda idx = i: write_slogan(idx))
            b15.grid(row=fila, column=columna)
        else:
            # botones blancos
            blanca = tk.Button(frame, width=2, height=1, bg = "white")
            blanca.grid(row=fila, column=columna)
        columna+=1
        i+=1
    fila+=30
root.mainloop()